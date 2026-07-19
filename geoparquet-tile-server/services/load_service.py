import geopandas as gpd
import pandas as pd
import pyarrow as pa
import pyarrow.dataset as ds
import h3
from pathlib import Path
from constants.tiles_constants import H3_LAKE_FOLDER, H3_PARTITION_RES


def load_gpkg_to_parquet_lake(file_name:str):
    '''
    - prototype function to breakdown canada building data in gpk format
    - normalizes meta data fields, sets geom to EPSG:4326
    - saves parquet files in h3_6 partioned folders 
    - this function can be used as a reference when creating a
      generlized function usable for reading multiple formats
      and a dynmaic set of meta data fields
    '''
    try:

        # read gpkg file
        gdf = to_gdf(file_name, "gpkg", "EPSG:4326")

        # clean fields
        gdf = gdf.replace("..", None)
        gdf["year_built"] = pd.to_numeric(gdf["year_built"], errors="coerce")

        # create h3_partion fields for later partioning
        #fix crs wrap in own function
        gdf = attach_h3_partition_to_gdf(gdf)

        # write to h3 indexed parquet files
        write_h3_parquet(gdf, file_name)
        
    except Exception as e:
        print("gpkg_to_parquet ERROR", e, file_name)
        return False
    else:
        print(f"gpkg_to_parquet FILE CREATED", file_name)
        return True

def to_gdf(file_name: str, file_ext: str, target_crs: str):
    '''
    reads geometry file and creates a geopandas data frame
    NOTE: assumes files are in the source-data folder
    '''

    ROOT_DIR = Path(__file__).resolve().parents[2]
    input_path = ROOT_DIR / f"source-data/ODB_v3/{file_name}.{file_ext}"
    gdf = gpd.read_file(input_path, use_arrow = True)
    gdf = gdf.to_crs(target_crs)
    return gdf

def attach_h3_partition_to_gdf(gdf:  gpd.GeoDataFrame):
    '''
    use geoseries centroid to calculate h3_res6 and assign to field h3_partition
    '''

    # Round-trip the data through a flat projection, ideally one which preserves area, such as Equal Area Cylindrical ('+proj=cea'):
    # https://gis.stackexchange.com/questions/372564/userwarning-when-trying-to-get-centroid-from-a-polygon-geopandas
    centroid_series = gpd.GeoSeries(gdf["geometry"]).to_crs('+proj=cea').centroid.to_crs(gdf.crs)
    gdf["h3_partition"] = centroid_series.apply(
        lambda c: h3.latlng_to_cell(c.y, c.x, H3_PARTITION_RES)
    )
    return gdf

def write_h3_parquet(gdf:  gpd.GeoDataFrame, file_name:str):
    '''
    gdf to pyarrow table
    '''
   
    arrow = gdf.to_arrow()
    table = pa.table(arrow)
    ds.write_dataset(
        table,
        H3_LAKE_FOLDER,
        format="parquet",
        partitioning=["h3_partition"],
        basename_template=f"{file_name}_part_{"{i}"}.parquet",
        existing_data_behavior="overwrite_or_ignore"

    )
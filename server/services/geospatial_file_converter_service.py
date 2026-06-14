import geopandas as gpd
import pandas as pd
import pyarrow as pa
import pyarrow.dataset as ds
import h3

h3_lake = "h3_lake/res_6/"
h3_partion_resolution = 6

def geojson_to_parquet (file_name):
    # deprecated test function
    try:
        # prepare input/output path
        input_path = f"files/input/{file_name}.geojson"
        output_path = f"files/output/{file_name}.parquet"

        # read geojson file
        geo_data_frame = gpd.read_file(input_path, use_arrow=True)
        geo_data_frame.set_crs(epsg=4326)

        # apply additional meta data for filtering 
        geo_data_frame["source"] = file_name

        # convert to parquet and store to file
        geo_data_frame.to_parquet(
            output_path,
            engine="pyarrow",
            index=False,
            schema_version="1.0.0"   # enables GeoParquet metadata
            )
        
    except Exception as e:
        print("geojson_to_parquet ERROR", e)
        return False
    else:
        print(f"geojson_to_parquet FILE CREATED", file_name)
        return True
    

def gpkg_to_parquet(file_name:str):
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
        print("gpkg_to_parquet ERROR", e)
        return False
    else:
        print(f"gpkg_to_parquet FILE CREATED", file_name)
        return True

def to_gdf(file_name: str, file_ext: str, target_crs: str):
    '''
    reads geometry file and creates a geopandas data frame
    '''

    input_path = f"files/input/{file_name}.{file_ext}"
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
        lambda c: h3.latlng_to_cell(c.y, c.x, h3_partion_resolution)
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
        h3_lake,
        format="parquet",
        partitioning=["h3_partition"],
        basename_template=f"{file_name}_part_{"{i}"}",
        existing_data_behavior="overwrite_or_ignore"

    )
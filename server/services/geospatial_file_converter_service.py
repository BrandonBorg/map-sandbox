import geopandas as gpd
import pyarrow as pa
import pyarrow.parquet as pq

def geojson_to_parquet (file_name):
    try:
        # prepare input/output path
        input_path = f"files/input/{file_name}.geojson"
        output_path = f"files/output/{file_name}.parquet"

        # read geojson file
        geo_data_frame = gpd.read_file(input_path, use_arrow=True)

        geo_data_frame["id"] = range(len(geo_data_frame))
        geo_data_frame["source"] = file_name

        # convert to pyarrow table
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
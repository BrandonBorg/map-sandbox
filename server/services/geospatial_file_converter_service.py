import geopandas as gpd

def geojson_to_parquet (file_name):
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
    
def gpkg_to_parquet (file_name):
    try:
        # prepare input/output path
        input_path = f"files/input/{file_name}.gpkg"
        output_path = f"files/output/{file_name}.parquet"

        # read geojson file
        gdf = gpd.read_file(input_path, use_arrow=True)

        # convert to parquet and store to file
        gdf.to_parquet(
            output_path,
            engine="pyarrow",
            index=False,
            schema_version="1.0.0"   # enables GeoParquet metadata
            )
        
    except Exception as e:
        print("gpkg_to_parquet ERROR", e)
        return False
    else:
        print(f"gpkg_to_parquet FILE CREATED", file_name)
        return True
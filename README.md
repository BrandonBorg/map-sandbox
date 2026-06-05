# map-sandbox

## Help

### server commands
https://fastapi.tiangolo.com/#create-it  
activate virtual env => .venv\scripts\activate   
install requirments => pip install -r requirements.txt          
start fast api => fastapi dev
stop virtual env => deactivate 

### helpful docs
https://geopandas.org/en/stable/docs/user_guide/io.html#to-arrow

## Pipelines

### reading geojson -> parquet 
files can be placed inside files/input folder to be read, converted, and outputed to files/output to later be read and stored inside of duckdb
-- files in these folders are ingored from git tracking.

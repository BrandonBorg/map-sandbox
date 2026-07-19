# GeoParquet Tile Server

This project provides a lightweight pipeline and tile serving backend for geospatial data ingesting GeoPackage (gpkg) data into an H3-partitioned GeoParquet lake, then serving vector tiles from it.

## Overview

### Project Structure

- api/ - FastAPI route definitions
- services/ - ingestion, parquet orchestration, and tile generation logic
- constants/ - shared configuration values
- h3_lake/ - partitioned parquet output data

### Typical Workflow

1. Place source geospatial files in the root source-data folder.
2. Run the ingestion (load) process to convert them into H3-partitioned parquet data.
3. Query the tile endpoints to retrieve vector tiles for the map client.

### Loading data to lake

The current pipeline pulls data from the source-data/ODB_v3 folder. The bulk load API can be used with a few files at a time, or with all files if desired, though ingestion currently takes a few seconds to minutes per file depending on the machine.

The process performs very minor cleanup, converts the GeoPackage into a GeoDataFrame, and applies a small amount of pandas-based cleanup. It then attaches an H3 partition field to the data, which is later used for partitioning. Once the GeoDataFrame is ready, it is written to the data lake and partitioned based on the assigned H3 index. At the time of writing, the H3 resolution is hard-coded to resolution 6.

### Tile Requests

When a tile request is received, the router forwards the requested z/x/y values to the service layer. The service uses the parquet orchestrator to find the relevant parquet files for the requested tile by converting the tile bounds into H3 indexes. The matching parquet files are then read and transformed into a vector tile response using DuckDB to be returned.

### Parquet Orchestrator

The parquet orchestrator is responsible for mapping a requested tile to the correct parquet datasets in the data lake.

It takes the tile coordinates and uses Mercantile and H3 logic to derive the set of H3 indexes that overlap the tile footprint. Those indexes are then converted into parquet file paths, which are passed back to the tile service for reading. This allows the system to fetch only the relevant partitioned parquet files instead of scanning the whole data lake.


## Requirements

Install the Python dependencies from the requirements file:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Server

Start the application with the repository virtual environment:

```powershell
./start_server.ps1
```

Or, if you prefer to run it directly:

```bash
../.venv/Scripts/python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000
```

The API will be available locally through the configured FastAPI host and port.


## Future Improvements
Lots of things to improve here, but happy with the prototype for now.

Potential areas for growth include:
- clean input data / improving ingestion speeds
- More flexible route and service interfaces so the server can support custom processing pipelines for different data sources or tile use cases.
- Support for multiple H3 resolutions, potentially combined with zoom level partitioning strategies for better performance and scalability.

## Notes

- Source datasets such as ODB v3 files are large and may need to be downloaded separately.
- The parquet lake is generated from source data and is intended for tile serving and analysis.

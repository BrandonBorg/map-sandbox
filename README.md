# Map Sandbox

This repository is intended as a place to explore different approaches to mapping, infrastructure, and spatial data solutions through experimentation.

## Project Structure

- `/app` Vite + React frontend used to render maps and test interface ideas
- `/geoparquet-tile-server` Python service for ingesting source data and serving vector tiles
- `/source-data` Data to be parsed and loaded into datalakes

## Experiments / Projects 

### 1. Geoparquet Tile Server
A simple vector tile pipeline is now in place, including a GeoParquet based data lake with H3 indexed partitioning. This provides a foundation for serving map data through a lightweight tile-server workflow.
Uses `/app` and `/geoparquet-tile-server`

https://github.com/user-attachments/assets/ec3d7d6f-6d9a-46a9-be76-8f5671aba2b9

## Data Pipeline

### GeoPackage / GeoJSON to Parquet

Source files can be placed in the source-data folder and ingested by the tile server pipeline. The pipeline converts them into H3-partitioned Parquet data for efficient tile serving.

> Large ODB v3 files are intentionally not tracked in git and should be downloaded separately from the Open Database of Buildings source. See the README in the source-data folder for more details.

## Running the App
Run /app and /geoparquet-tile-server

## Helpful References

- FastAPI: https://fastapi.tiangolo.com/
- GeoPandas: https://geopandas.org/
- GeoParquet / Arrow: https://geopandas.org/en/stable/docs/user_guide/io.html#to-arrow
- Vector tile pipelines / https://www.vector-tile.com/


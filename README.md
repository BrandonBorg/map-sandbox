# map-sandbox

This repository is a personal sandbox for learning and prototyping in the geospatial space. It is intended as a place to explore different approaches to mapping, infrastructure, and spatial data solutions through experimentation.

## Project Structure

- app/ - Vite + React frontend used to render maps and test interface ideas
- geoparquet-tile-server/ - Python service for ingesting source data and serving vector tiles
- source-data/ - Source GeoPackage and GeoJSON datasets used for experimentation

## Current Focus

The current work centers on building and testing a vector tile pipeline using GeoParquet and H3-partitioned data as a practical foundation for exploration.

## Data Pipeline

### GeoPackage / GeoJSON to Parquet

Source files can be placed in the source-data folder and ingested by the tile server pipeline. The pipeline converts them into H3-partitioned Parquet data for efficient tile serving.

> Large ODB v3 files are intentionally not tracked in git and should be downloaded separately from the Open Database of Buildings source. See the README in the source-data folder for more details.

## Running the App

### Frontend

From the app folder:

```bash
npm install
npm run dev
```

### Tile Server

From the geoparquet-tile-server folder:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Helpful References

- FastAPI: https://fastapi.tiangolo.com/
- GeoPandas: https://geopandas.org/
- GeoParquet / Arrow: https://geopandas.org/en/stable/docs/user_guide/io.html#to-arrow



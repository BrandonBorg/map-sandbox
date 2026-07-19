import React, { useRef, useEffect } from "react";
import maplibregl, {Map}  from "maplibre-gl"
import "maplibre-gl/dist/maplibre-gl.css";
import "./TestMap.css"
export default function TestMap()
{
    const mapContainer = useRef<HTMLDivElement| null>(null);
    const mapGL = useRef<Map|null>(null);

    // on component init render
    useEffect(()=>
    {
        if(!mapContainer.current)
        {
            return
        }
        
        const map = new maplibregl.Map({
            container: mapContainer.current, // container id
             style: {
            version: 8,
            sources: {
                'odb_v3': {
                    type: 'vector',
                    // geoparquet tile server endpoint
                    tiles: [`http://127.0.0.1:8000/v1/tiles/{z}/{x}/{y}`],
                    minzoom: 11
                },
                // Also use a public open source basemap
                'osm': {
                    type: 'raster',
                    tiles: [
                        'https://a.tile.openstreetmap.org/{z}/{x}/{y}.png',
                        'https://b.tile.openstreetmap.org/{z}/{x}/{y}.png',
                        'https://c.tile.openstreetmap.org/{z}/{x}/{y}.png'
                    ],
                    tileSize: 256,
                    minzoom: 2
                }
            },
            layers: [
                {
                    id: 'background',
                    type: 'background',
                    paint: { 'background-color': '#a0c8f0' }
                },
                {
                    id: 'osm',
                    type: 'raster',
                    source: 'osm',
                    minzoom: 2,
                },
                {
                    id: 'simple_geometry-fill',
                    type: 'fill',
                    source: 'odb_v3',
                    'source-layer': 'odb_v3',
                    paint: {
                        'fill-color': 'blue',
                        'fill-opacity': 0.6,
                        'fill-outline-color': '#ffffff'
                    }
                },
                {
                    id: 'simple_geometry-stroke',
                    type: 'line',
                    source: 'odb_v3',
                    'source-layer': 'odb_v3',
                    paint: {
                        'line-color': 'black',
                        'line-width': 0.5
                    }
                }
            ]
        },
          center: [-79.347015, 43.651070],
            zoom: 18
        })

        map.showTileBoundaries = true;
        map.showCollisionBoxes = true;

        // todo fix this
        mapGL.current = map;
      
    },[])
    

    return (
        <div className="map-wrap">
            <div ref={mapContainer} className="map"/>
        </div>
    )
}
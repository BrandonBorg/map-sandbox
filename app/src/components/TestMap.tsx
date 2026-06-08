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
                'simple_geometry': {
                    type: 'vector',
                    tiles: [`http://127.0.0.1:8000/v1/tiles/simple_geometry/{z}/{x}/{y}`],
                    minzoom: 2
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
                    maxzoom: 19
                },
                {
                    id: 'simple_geometry-fill',
                    type: 'fill',
                    source: 'simple_geometry',
                    'source-layer': 'simple_geometry',
                    paint: {
                        'fill-color': 'blue',
                        'fill-opacity': 0.6,
                        'fill-outline-color': '#ffffff'
                    }
                },
                {
                    id: 'simple_geometry-stroke',
                    type: 'line',
                    source: 'simple_geometry',
                    'source-layer': 'simple_geometry',
                    paint: {
                        'line-color': 'black',
                        'line-width': 0.5
                    }
                }
            ]
        },
          center: [-63.1311, 46.2382],
            zoom: 12
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
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
            console.log("oops")
            return
        }
        console.log("map hit")
        
        mapGL.current = new maplibregl.Map({
        container: mapContainer.current, // container id
        style: "https://demotiles.maplibre.org/globe.json", // style URL
        center: [0, 0], // starting position [lng, lat]
        zoom: 1 // starting zoom
    })
    },[])
    

    return (
        <div className="map-wrap">
            <div ref={mapContainer} className="map"/>
        </div>
    )
}
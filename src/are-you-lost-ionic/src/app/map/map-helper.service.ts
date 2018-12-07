import {Injectable} from '@angular/core';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/of';

import leaflet from 'leaflet'

@Injectable()
export class MapHelperService{
   public map;

   initMap(){
     this.map = new leaflet.Map("map");
     this.map.setView(new leaflet.LatLng(31.585692323629303, 35.19333585601518), 2);
     leaflet.tileLayer(`https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png`, {
             maxZoom: 20,
             attribution: 'HOT',
          }).addTo(this.map);
   } 
   drawPoints(data){
      // points
      data.points.forEach(p=>this.addMarker(p.pos.lat, p.pos.lon));
      // lines
      data.lines.forEach(l=>{
        // src
        this.addMarker(l.pos.src.lat, l.pos.src.lon);
        // dest
        this.addMarker(l.pos.dest.lat, l.pos.dest.lon);
        // line       
        this.addLine(l.pos.src, l.pos.dest);             
      });
   }
   addMarker(lat,lng){
    let m = leaflet.marker([lat,lng]).addTo(this.map);
   }
   addLine(src, dest) {
         let line = leaflet.polyline(
                [
                    [src.lat, src.lon],
                    [dest.lat, dest.lon]
                ],
                {color: 'red'}
         ).addTo(this.map)
   }
}
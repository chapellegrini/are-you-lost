/*
import {Injectable} from '@angular/core';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/of';

import leaflet from 'leaflet'

@Injectable()
export class MapHelperService{
   public map;

   initMap(){
     this.map = new leaflet.Map("map");
	 //this.map.setView(new leaflet.LatLng(31.585692323629303, 35.19333585601518), 2);
	this.map.locate({ setView: true, zoom: 10 });
	this.map.on('locationfound', this.onLocationFound.bind(this));
	//this.map.on('locationerror', this.onLocationError.bind(this));
	 
     leaflet.tileLayer(`https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png`, {
             maxZoom: 20,
             attribution: 'HOT',
          }).addTo(this.map);
   } 

   public onLocationFound(e) {
   		var radius = e.accuracy / 2;
		leaflet.marker(e.latlng).addTo(this.map);
		leaflet.circle(e.latlng, radius).addTo(this.map);
   }

   public onLocationError(e) {
   		console.log(e);
		alert(e.message || 'something is wrong');
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
*/
import {Injectable} from '@angular/core';



import { Observable } from 'rxjs/Observable';

import 'rxjs/add/observable/of';



import leaflet from 'leaflet'

import { HttpClient, HttpHeaders } from '@angular/common/http';





@Injectable()

export class MapHelperService{

   public map;



   initMap(){

     this.map = new leaflet.Map("map");    

     this.map.locate({ setView: true, zoom: 10 }); 

     

     this.map.on('locationfound', this.onLocationFound.bind(this));

     this.map.on('locationerror', this.onLocationError.bind(this));

     leaflet.tileLayer(`https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png`, {

             maxZoom: 20,

             attribution: 'HOT',

          }).addTo(this.map); 

   } 



   public onLocationFound(e) {

    var radius = e.accuracy / 2;

    var m = leaflet.marker(e.latlng).addTo(this.map); 

    m.bindPopup("<b>I'm here!</b><br>").openPopup();

      

    leaflet.circle(e.latlng, radius).addTo(this.map);

  }



  private onLocationError(e) {

    console.log(e);

    alert(e.message || 'something is wrong');

  }



/*

  public display(m) {

    var string='';

    string = "name : " + m.name;

    string += "<br>";

    string+= "lat : " + m.pos.lattitude;

    string += "<br>";

    string+= "lat : " + m.pos.longitude;

    for (var item in m.inventory){

      string += item + ' ';

      string += m.inventory[item];

      string += '<br>';

    }

    return string

  }*/



   drawPoints(data){

      // points

      data.points.forEach(p=>this.addMarker(p.pos.lat, p.pos.lon,p));

      // lines

      data.lines.forEach(l=>{

        // src

        this.addMarker(l.pos.src.lat, l.pos.src.lon,l);

        // dest 

        this.addMarker(l.pos.dest.lat, l.pos.dest.lon,l);

        // line       

        this.addLine(l.pos.src, l.pos.dest);             

      });

   }

   addMarker(lat,lng,p){

    var m = leaflet.marker([lat,lng]).addTo(this.map);

    /*m.bindPopup(this.display(p)).openPopup();*/

    m.bindPopup(p.type).openPopup();

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

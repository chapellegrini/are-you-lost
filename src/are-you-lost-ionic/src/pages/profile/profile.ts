import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';

@Component({
  selector: 'page-profile',
  templateUrl: 'profile.html'
})
export class ProfilePage {
  name: string;
  lon: number;
  lat: number;

  constructor(public navCtrl: NavController) {

 	this.name="Jean-Luc";

	this.lon = 10;
	this.lat = 20;
  	
  }

}

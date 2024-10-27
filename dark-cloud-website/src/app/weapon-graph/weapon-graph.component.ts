import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import * as shape from 'd3-shape';
import { NgxGraphModule } from '@swimlane/ngx-graph';

@Component({
  selector: 'weapon-graph',
  templateUrl: './weapon-graph.component.html',
  styleUrls: [ './weapon-graph.component.scss' ]
})
export class WeaponGraphComponent  {
  name = 'Angular 5';
  hierarchialGraph = {nodes: [], links: []}
  curve = shape.curveBundle.beta(1);
  weaponUrlRoot: string = './api/weapons/images/';
  // weaponUrlRoot: string = 'https://s3-us-west-2.amazonaws.com/dark-cloud-bucket-dev/weapons/images/';
  // curve = shape.curveLinear;kk

  public ngOnInit():void {
    this.showGraph();
  }

  showGraph() {
    this.hierarchialGraph.nodes = [
  {
    id: 'start',
    label: 'Jackal',
    position: 'x0',
    weaponThumbnail: 'Osmond_Jackal_Thumbnail.jpg'
    //weaponThumbnail: "Osmond_Jackal_Thumbnail.jpg"
  }, {
    id: '1',
    label: 'Blessing Gun',
    position: 'x1',
    weaponThumbnail: 'Osmond_Blessing_Gun_Thumbnail.jpg'
  }, {
    id: '2',
    label: 'Swallow',
    position: 'x2',
    weaponThumbnail: 'Osmond_Swallow_Thumbnail.jpg'
  }, {
    id: '3',
    label: 'Skunk',
    position: 'x3',
    weaponThumbnail: 'Osmond_Skunk_Thumbnail.jpg'
  }, {
    id: '4',
    label: 'G Crusher',
    position: 'x4',
    weaponThumbnail: 'Osmond_G_Crusher_Thumbnail.jpg'
  }, {
    id: '5',
    label: 'Hexa Blaster',
    position: 'x5',
    weaponThumbnail: 'Osmond_Hexa_Blaster_Thumbnail.jpg'
  }, {
    id: '6',
    label: 'Supernova',
    position: 'x6',
    weaponThumbnail: 'Osmond_Supernova_Thumbnail.jpg'
  }, {
    id: '7',
    label: 'Star Breaker',
    position: 'x7',
    weaponThumbnail: 'Osmond_Star_Breaker_Thumbnail.jpg'
  }, {
    id: 'snail',
    label: 'snail',
    position: 'x0',
    weaponThumbnail: 'Osmond_Snail_thumbnail.jpg'
  }

  ];

  this.hierarchialGraph.links = [
  {
    source: 'start',
    target: '1',
    label: 'Process#1'
  }, {
    source: 'start',
    target: '2',
    label: 'Process#2'
  }, {
    source: '1',
    target: '3',
    label: 'Process#3'
  }, {
    source: '2',
    target: '4',
    label: 'Process#4'
  }, {
    source: '5',
    target: '6',
    label: 'Process#6'
  }, {
    source: '3',
    target: '5'
  }, {
    source: '4',
    target: '7',
    label: 'Process#7'
  }, {
    source: 'snail',
    target: '1',
    label: 'snail->blessing'
  }, {
    source: 'snail',
    target: '5',
    label: 'snail->hexa blaster'
  }
  ];

  }
}

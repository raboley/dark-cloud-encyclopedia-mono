import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import * as shape from 'd3-shape';

@Component({
  selector: 'weapon-graph',
  templateUrl: './weapon-graph.component.html',
  styleUrls: ['./weapon-graph.component.scss']
})
export class WeaponGraphComponent implements OnInit {
  name = 'Angular 5';
  hierarchialGraph = { nodes: [], links: [] };
  curve = shape.curveBundle.beta(1);
  weaponUrlRoot: string = './api/weapons/images/';
  characters: string[] = ['Osmond', 'Xiao'];
  selectedCharacter: string = this.characters[0];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadConfig();
  }

  loadConfig(): void {
    this.http.get<{ weaponUrlRoot: string }>('./assets/config.json').subscribe(config => {
      this.weaponUrlRoot = config.weaponUrlRoot;
    });
    this.showGraph();
  }

  onCharacterChange(event: Event): void {
    const selectElement = event.target as HTMLSelectElement;
    this.selectedCharacter = selectElement.value;
    this.showGraph();
  }

  showGraph() {
    console.log('selectedCharacter', this.selectedCharacter);
    if (this.selectedCharacter === 'Osmond') {
      this.hierarchialGraph.nodes = [
        { id: 'start', label: 'Jackal', position: 'x0', weaponThumbnail: `Osmond_Jackal_Thumbnail.jpg` },
        { id: '1', label: 'Blessing Gun', position: 'x1', weaponThumbnail: `Osmond_Blessing_Gun_Thumbnail.jpg` },
        { id: '2', label: 'Swallow', position: 'x2', weaponThumbnail: `Osmond_Swallow_Thumbnail.jpg` },
        { id: '3', label: 'Skunk', position: 'x3', weaponThumbnail: `Osmond_Skunk_Thumbnail.jpg` },
        { id: '4', label: 'G Crusher', position: 'x4', weaponThumbnail: `Osmond_G_Crusher_Thumbnail.jpg` },
        { id: '5', label: 'Hexa Blaster', position: 'x5', weaponThumbnail: `Osmond_Hexa_Blaster_Thumbnail.jpg` },
        { id: '6', label: 'Supernova', position: 'x6', weaponThumbnail: `Osmond_Supernova_Thumbnail.jpg` },
        { id: '7', label: 'Star Breaker', position: 'x7', weaponThumbnail: `Osmond_Star_Breaker_Thumbnail.jpg` },
        { id: 'snail', label: 'snail', position: 'x0', weaponThumbnail: `Osmond_Snail_thumbnail.jpg` }
      ];

      this.hierarchialGraph.links = [
        { source: 'start', target: '1', label: 'Process#1' },
        { source: 'start', target: '2', label: 'Process#2' },
        { source: '1', target: '3', label: 'Process#3' },
        { source: '2', target: '4', label: 'Process#4' },
        { source: '5', target: '6', label: 'Process#6' },
        { source: '3', target: '5' },
        { source: '4', target: '7', label: 'Process#7' },
        { source: 'snail', target: '1', label: 'snail->blessing' },
        { source: 'snail', target: '5', label: 'snail->hexa blaster' }
      ];
    } else if (this.selectedCharacter === 'Xiao') {
      this.hierarchialGraph.nodes = [
        { id: 'start', label: 'Bandit Slingshot', position: 'x0', weaponThumbnail: `Xiao_Bandit_Slingshot_Thumbnail.jpg` },
        { id: '1', label: 'Hardshooter', position: 'x1', weaponThumbnail: `Xiao_Hardshooter_Thumbnail.jpg` },
        { id: '2', label: 'Double Impact', position: 'x2', weaponThumbnail: `Xiao_Double_Impact_Thumbnail.jpg` },
        { id: '3', label: 'Bone Slingshot', position: 'x3', weaponThumbnail: `Xiao_Bone_Slingshot_Thumbnail.jpg` },
        { id: '4', label: 'Flamingo', position: 'x4', weaponThumbnail: `Xiao_Flamingo_Thumbnail.jpg` },
        { id: '5', label: 'Steel Slingshot', position: 'x5', weaponThumbnail: `Xiao_Steel_Slingshot_Thumbnail.jpg` },
        { id: '6', label: 'Dragon\'s Y', position: 'x6', weaponThumbnail: `Xiao_Dragons_Y_Thumbnail.jpg` },
        { id: '7', label: 'Matador', position: 'x7', weaponThumbnail: `Xiao_Matador_Thumbnail.jpg` },
        { id: '8', label: 'Divine Beast Title', position: 'x8', weaponThumbnail: `Xiao_Divine_Beast_Title_Thumbnail.jpg` },
        { id: '9', label: 'Angel Shooter', position: 'x9', weaponThumbnail: `Xiao_Angel_Shooter_Thumbnail.jpg` },
        { id: '10', label: 'Angel Gear', position: 'x10', weaponThumbnail: `Xiao_Angel_Gear_Thumbnail.jpg` },
        { id: '11', label: 'Steve', position: 'x11', weaponThumbnail: `Xiao_Steve_Thumbnail.jpg` },
        { id: '12', label: 'Super Steve', position: 'x12', weaponThumbnail: `Xiao_Super_Steve_Thumbnail.jpg` }
      ];

      this.hierarchialGraph.links = [
        { source: 'start', target: '1', label: 'Process#1' },
        { source: 'start', target: '2', label: 'Process#2' },
        { source: '3', target: '4', label: 'Process#3' },
        { source: '5', target: '1', label: 'Process#4' },
        { source: '4', target: '6', label: 'Process#5' },
        { source: '1', target: '2', label: 'Process#6' },
        { source: '1', target: '7', label: 'Process#7' },
        { source: '2', target: '8', label: 'Process#8' },
        { source: '6', target: '8', label: 'Process#9' },
        { source: '7', target: '8', label: 'Process#10' },
        { source: '8', target: '9', label: 'Process#11' },
        { source: '9', target: '10', label: 'Process#12' },
        { source: '11', target: '12', label: 'Process#13' }
      ];
    }
  }
}

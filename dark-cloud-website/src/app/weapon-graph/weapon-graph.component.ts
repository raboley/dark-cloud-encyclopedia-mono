// src/app/weapon-graph/weapon-graph.component.ts
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
  characters: string[] = ['Toan', 'Osmond', 'Xiao'];
  selectedCharacter: string = this.characters[0];
  weaponGraphs: any = {};

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadConfig();
  }

  loadConfig(): void {
    this.http.get<{ weaponUrlRoot: string }>('./assets/config.json').subscribe(config => {
      this.weaponUrlRoot = config.weaponUrlRoot;
    });
    this.loadWeaponGraphs();
  }

  loadWeaponGraphs(): void {
    this.http.get('./assets/weapon-graphs.json').subscribe(graphs => {
      this.weaponGraphs = graphs;
      this.characters = Object.keys(this.weaponGraphs);
      this.selectedCharacter = this.characters[0];
      this.showGraph();
    });
  }

  onCharacterChange(event: Event): void {
    const selectElement = event.target as HTMLSelectElement;
    this.selectedCharacter = selectElement.value;
    this.showGraph();
  }

  showGraph() {
    console.log('selectedCharacter', this.selectedCharacter);
    const graph = this.weaponGraphs[this.selectedCharacter];
    if (graph) {
      this.hierarchialGraph.nodes = graph.nodes;
      this.hierarchialGraph.links = graph.links;
    }
  }

  hasDims(): boolean {
    return this.hierarchialGraph.nodes.length > 0 && this.hierarchialGraph.links.length > 0;
  }
}

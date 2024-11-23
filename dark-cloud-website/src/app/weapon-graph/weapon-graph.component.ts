import { Component, OnInit, AfterViewInit, ChangeDetectorRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import * as shape from 'd3-shape';
import { Subject } from 'rxjs';

@Component({
  selector: 'weapon-graph',
  templateUrl: './weapon-graph.component.html',
  styleUrls: ['./weapon-graph.component.scss']
})
export class WeaponGraphComponent implements OnInit, AfterViewInit {
  name = 'Angular 5';
  hierarchialGraph = { nodes: [], links: [] };
  curve = shape.curveBundle.beta(1);
  weaponUrlRoot = './api/weapons/images/';
  characters = ['Toan', 'Osmond', 'Xiao'];
  selectedCharacter = this.characters[0];
  weaponGraphs: any = {};
  zoomToFit$ = new Subject<boolean>();

  constructor(private http: HttpClient, private cdr: ChangeDetectorRef) {}
filterByCharacter(character: string): void {
  this.selectedCharacter = character;
  this.showGraph();
}
  ngOnInit(): void {
    this.loadConfig();
  }

  ngAfterViewInit(): void {
    setTimeout(() => {
      this.zoomToFit$.next(true); // Trigger auto-centering after view initialization
      this.cdr.detectChanges(); // Manually trigger change detection
    }, 100); // Add a slight delay
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
      setTimeout(() => {
        this.zoomToFit$.next(true); // Trigger auto-centering after updating the graph
        this.cdr.detectChanges(); // Manually trigger change detection
      }, 100); // Add a slight delay
    }
  }

  hasDims(): boolean {
    return this.hierarchialGraph.nodes.length > 0 && this.hierarchialGraph.links.length > 0;
  }

  stopEvent(event: Event): void {
    event.stopPropagation();
  }
}

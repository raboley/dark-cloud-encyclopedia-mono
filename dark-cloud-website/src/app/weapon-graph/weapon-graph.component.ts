import { Component, OnInit, AfterViewInit, ChangeDetectorRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import * as shape from 'd3-shape';
import { Subject } from 'rxjs';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'pm-weapon-graph',
  templateUrl: './weapon-graph.component.html',
  styleUrls: ['./weapon-graph.component.scss']
})
export class WeaponGraphComponent implements OnInit, AfterViewInit {
  name = 'Angular 5';
  hierarchialGraph = { nodes: [], links: [] };
  curve = shape.curveBundle.beta(1);
  weaponUrlRoot = './api/weapons/images/';
  characters = ['Toan', 'Goro', 'Ruby', 'Ungaga', 'Osmond', 'Xiao'];
  selectedCharacter = this.characters[0];
  weaponGraphs: any = {};
  zoomToFit$ = new Subject<boolean>();

  constructor(
    private http: HttpClient,
    private cdr: ChangeDetectorRef,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      const character = params['character'];
      console.log('character', character);
      if (character && this.characters.includes(character)) {
        console.log('Setting selected character to', character);
        this.selectedCharacter = character;
      }
      this.loadConfig();
      this.setHostHeight(); // Set the height based on the selected character
    });
  }

setHostHeight(): void {
  const hostElement = document.querySelector('pm-weapon-graph') as HTMLElement;
  if (hostElement) {
    if (this.selectedCharacter === 'Toan') {
      hostElement.style.height = '2000px';
    } else {
      hostElement.style.height = '100vh'; // Default height for other characters
    }
  }
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
      console.log('selected character', this.selectedCharacter);
      if (!this.characters.includes(this.selectedCharacter)) {
        console.log('Character {} not found, defaulting to first character', this.selectedCharacter);
        this.selectedCharacter = this.characters[0];
      }
      this.showGraph();
      this.setHostHeight(); // Set the height based on the selected character
    });
  }

  onCharacterChange(character: string): void {
    this.selectedCharacter = character;
    this.router.navigate([], {
      relativeTo: this.route,
      queryParams: { character: this.selectedCharacter },
      queryParamsHandling: 'merge'
    }).then(() => {
      this.showGraph();
    });
  }

  showGraph(): void {
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

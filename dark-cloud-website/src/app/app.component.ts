import { Component, ViewChild } from '@angular/core';
import { Subject } from 'rxjs';
import { WeaponGraphComponent } from './weapon-graph/weapon-graph.component';

@Component({
  selector: 'pm-root',
  template: `
    <nav class='navbar navbar-expand navbar-light bg-light'>
        <a class='navbar-brand'>{{pageTitle}}</a>
        <ul class='nav nav-pills'>
          <li><a class='nav-link' routerLinkActive='active' [routerLink]="['/weapon-graph']">Home</a></li>
          <li><a class='nav-link' routerLinkActive='active' [routerLink]="['/weapons']">Weapon List</a></li>
          <li><a class='nav-link' routerLinkActive='active' [routerLink]="['/image-checklist']">Image Checklist</a></li>
        </ul>
    </nav>
    <div class='container-fluid'>
      <router-outlet></router-outlet>
    </div>
  `,
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  pageTitle = 'Dark Cloud Encyclopedia';
  @ViewChild(WeaponGraphComponent) graphRef: WeaponGraphComponent;
  zoomToFit$ = new Subject<{ autoCenter: boolean, force: boolean }>();
  isLoading = true;

  handleStateChange(event: any) {
    if (event.state === 'Transform' && this.graphRef && this.graphRef.hasDims()) {
      this.zoomToFit$.next({ autoCenter: true, force: true });
      this.isLoading = false;
    }
  }
}

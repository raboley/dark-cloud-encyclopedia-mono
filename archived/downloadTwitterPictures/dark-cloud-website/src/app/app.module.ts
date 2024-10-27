import { BrowserModule } from '@angular/platform-browser';
import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { WelcomeComponent } from './home/welcome.component';
import { WeaponModule } from './weapons/weapon.module';
import { RouterModule } from '@angular/router';
import { WeaponGraphComponent } from './weapon-graph/weapon-graph.component';

import { NgxGraphModule } from '@swimlane/ngx-graph';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule } from '@angular/forms';
import { ImageChecklistModule } from './image-checklist/image-checklist.module';

@NgModule({
  declarations: [
    AppComponent,
    WelcomeComponent,
    WeaponGraphComponent
  ],
  imports: [
    RouterModule.forRoot([
      { path: 'welcome', component: WelcomeComponent },
      { path: '', redirectTo: 'welcome', pathMatch: 'full' },
      { path: '**', redirectTo: 'welcome', pathMatch: 'full' }
    ]),
    BrowserModule,
    HttpClientModule,
    WeaponModule,
    FormsModule, NgxGraphModule, NgxChartsModule,BrowserAnimationsModule, ImageChecklistModule
  ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  bootstrap: [AppComponent]
})
export class AppModule { }

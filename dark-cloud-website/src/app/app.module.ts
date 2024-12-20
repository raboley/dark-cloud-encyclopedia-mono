import { BrowserModule } from "@angular/platform-browser";
import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from "@angular/core";
import { HttpClientModule } from "@angular/common/http";

import { AppComponent } from "./app.component";
import { WelcomeComponent } from "./home/welcome.component";
import { WeaponModule } from "./weapons/weapon.module";
import { RouterModule } from "@angular/router";
import { WeaponGraphComponent } from "./weapon-graph/weapon-graph.component";
import { WeaponGraphPageComponent } from "./weapon-graph-page/weapon-graph-page.component";

import { NgxGraphModule } from "@swimlane/ngx-graph";
import { NgxChartsModule } from "@swimlane/ngx-charts";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { FormsModule } from "@angular/forms";
import { ImageChecklistModule } from "./image-checklist/image-checklist.module";
import { ImageModalModule } from "./image-modal/image-modal.module";

@NgModule({
  declarations: [
    AppComponent,
    WelcomeComponent,
    WeaponGraphComponent,
    WeaponGraphPageComponent,
  ],
  imports: [
    RouterModule.forRoot([
      { path: "weapon-graph", component: WeaponGraphComponent },
      { path: "", redirectTo: "weapon-graph", pathMatch: "full" },
      { path: "**", redirectTo: "weapon-graph", pathMatch: "full" },
    ]),
    BrowserModule,
    HttpClientModule,
    WeaponModule,
    FormsModule,
    NgxGraphModule,
    NgxChartsModule,
    BrowserAnimationsModule,
    ImageChecklistModule,
    ImageModalModule,
  ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  bootstrap: [AppComponent],
})
export class AppModule {}

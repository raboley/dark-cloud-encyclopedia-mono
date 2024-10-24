import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ImageChecklistRoutingModule } from './image-checklist-routing.module';
import { ImageChecklistComponent } from './image-checklist.component';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [ImageChecklistComponent],
  imports: [
    CommonModule,
    ImageChecklistRoutingModule,
    HttpClientModule
  ]
})
export class ImageChecklistModule { }

import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ImageChecklistComponent } from './image-checklist.component';

const routes: Routes = [{ path: 'image-checklist', component: ImageChecklistComponent },];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ImageChecklistRoutingModule { }

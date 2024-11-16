// src/app/image-modal/image-modal.module.ts
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageModalComponent } from './image-modal.component';

@NgModule({
  declarations: [ImageModalComponent],
  imports: [CommonModule],
  exports: [ImageModalComponent]
})
export class ImageModalModule { }

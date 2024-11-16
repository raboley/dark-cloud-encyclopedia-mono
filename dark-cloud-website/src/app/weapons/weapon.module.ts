import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WeaponListComponent } from './weapon-list.component';
import { WeaponDetailComponent } from './weapon-detail.component';
import { ConvertToSpacesPipe } from '../shared/convert-to-spaces.pipe';
import { WeaponDetailGuard } from './weapon-detail.guard';
import { SharedModule } from '../shared/shared.module';
import { WeaponDetailImagesComponent } from './weapon-detail-images/weapon-detail-images.component';
import { ImageModalModule } from '../image-modal/image-modal.module';


@NgModule({
  imports: [
    RouterModule.forChild([
      { path: 'weapons', component: WeaponListComponent },
      {
        path: 'weapons/:id',
        canActivate: [WeaponDetailGuard],
        component: WeaponDetailComponent
      },
    ]),
    SharedModule,
    ImageModalModule
  ],
  declarations: [
    WeaponListComponent,
    WeaponDetailComponent,
    ConvertToSpacesPipe,
    WeaponDetailImagesComponent,
  ]
})
export class WeaponModule { }

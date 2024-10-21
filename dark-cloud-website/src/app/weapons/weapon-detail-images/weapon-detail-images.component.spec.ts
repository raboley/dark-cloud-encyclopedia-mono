import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WeaponDetailImagesComponent } from './weapon-detail-images.component';

describe('WeaponDetailImagesComponent', () => {
  let component: WeaponDetailImagesComponent;
  let fixture: ComponentFixture<WeaponDetailImagesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WeaponDetailImagesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WeaponDetailImagesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  xit('should create', () => {
    expect(component).toBeTruthy();
  });
});

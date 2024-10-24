import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WeaponGraphComponent } from './weapon-graph.component';

describe('WeaponGraphComponent', () => {
  let component: WeaponGraphComponent;
  let fixture: ComponentFixture<WeaponGraphComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WeaponGraphComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WeaponGraphComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});

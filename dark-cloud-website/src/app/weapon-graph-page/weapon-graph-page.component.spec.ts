import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WeaponGraphPageComponent } from './weapon-graph-page.component';

describe('WeaponGraphPageComponent', () => {
  let component: WeaponGraphPageComponent;
  let fixture: ComponentFixture<WeaponGraphPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WeaponGraphPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WeaponGraphPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

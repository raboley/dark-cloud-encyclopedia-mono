import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ImageChecklistComponent } from './image-checklist.component';

describe('ImageChecklistComponent', () => {
  let component: ImageChecklistComponent;
  let fixture: ComponentFixture<ImageChecklistComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ImageChecklistComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ImageChecklistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});

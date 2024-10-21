import { TestBed, async, inject } from '@angular/core/testing';

import { WeaponDetailGuard } from './weapon-detail.guard';

describe('WeaponDetailGuard', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [WeaponDetailGuard]
    });
  });

  xit('should ...', inject([WeaponDetailGuard], (guard: WeaponDetailGuard) => {
    expect(guard).toBeTruthy();
  }));
});

import { WeaponModule } from './weapon.module';

describe('WeaponModule', () => {
  let weaponModule: WeaponModule;

  beforeEach(() => {
    weaponModule = new WeaponModule();
  });

  xit('should create an instance', () => {
    expect(weaponModule).toBeTruthy();
  });
});

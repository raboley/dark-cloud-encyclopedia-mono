import { Component, OnInit } from '@angular/core';
import { IWeapon } from '../weapon';
import { ActivatedRoute, Router } from '@angular/router';
import { WeaponService } from '../weapon.service';

@Component({
  selector: 'pm-weapon-detail-images',
  templateUrl: './weapon-detail-images.component.html',
  styleUrls: ['./weapon-detail-images.component.css']
})
export class WeaponDetailImagesComponent implements OnInit {
  pageTitle = 'Weapon Detail';
  errorMessage = '';
  weapon: IWeapon | undefined;
  weaponUrls: string | undefined;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private weaponService: WeaponService
  ) {}

  ngOnInit() {
    const param = this.route.snapshot.paramMap.get('id');
    if (param) {
      const id = +param;
      this.getWeapon(id);
    }
  }

  getWeapon(id: number) {
    this.weaponService.getWeapon(id).subscribe(
      weapon => {
        this.weapon = weapon;
        this.getWeaponUrls(this.weapon.characterName, this.weapon.weaponName);
      },
      error => (this.errorMessage = <any>error)
    );
  }

  getWeaponUrls(characterName: string, weaponName: string) {
    this.weaponUrls = `./api/weapons/images/${characterName}_${weaponName}_Stats.jpg`;
  }

  onBack(): void {
    this.router.navigate(['/weapons']);
  }
}

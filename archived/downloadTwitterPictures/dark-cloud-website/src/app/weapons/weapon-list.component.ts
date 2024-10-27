import { Component, OnInit } from '@angular/core';

import { IWeapon } from './weapon';
import { WeaponService } from './weapon.service';

@Component({
  templateUrl: './weapon-list.component.html',
  styleUrls: ['./weapon-list.component.css']
})
export class WeaponListComponent implements OnInit {
  pageTitle = 'Weapon List';
  imageWidth = 50;
  imageMargin = 2;
  showImage = true;
  errorMessage = '';
  weaponUrlRoot: string = 'https://s3-us-west-2.amazonaws.com/dark-cloud-bucket-dev/weapons/images/';
  //weaponUrlRoot: string = 'https://s3-us-west-2.amazonaws.com/dark-cloud-bucket2/weapons/images/'


  _listFilter = '';
  get listFilter(): string {
    return this._listFilter;
  }
  set listFilter(value: string) {
    this._listFilter = value;
    this.filteredWeapons = this.listFilter ? this.performFilter(this.listFilter) : this.weapons;
  }

  filteredWeapons: IWeapon[] = [];
  weapons: IWeapon[] = [];

  constructor(private weaponService: WeaponService) {

  }

  onRatingClicked(message: string): void {
    this.pageTitle = 'Weapon List: ' + message;
  }

  performFilter(filterBy: string): IWeapon[] {
    filterBy = filterBy.toLocaleLowerCase();
    return this.weapons.filter((weapon: IWeapon) =>
      weapon.weaponName.toLocaleLowerCase().indexOf(filterBy) !== -1);
  }

  toggleImage(): void {
    this.showImage = !this.showImage;
  }

  ngOnInit(): void {
    this.weaponService.getWeapons().subscribe(
      weapons => {
        this.weapons = weapons;

        this.filteredWeapons = this.weapons;
      },
      error => this.errorMessage = <any>error
    );
  }
}

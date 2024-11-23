import { Component, OnInit } from '@angular/core';

import { IWeapon } from './weapon';
import { WeaponService } from './weapon.service';

@Component({
  templateUrl: './weapon-list.component.html',
  styleUrls: ['./weapon-list.component.css']
})
export class WeaponListComponent implements OnInit {
  pageTitle = 'Weapon List';
  imageMargin = 2;
  showImage = true;
  errorMessage = '';
  weaponUrlRoot: string = './api/weapons/images/';
  characters: string[] = ['Goro', 'Osmond', 'Ruby', 'Toan', 'Ungaga', 'Xiao'];
  selectedCharacter: string | null = null;

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

  constructor(private weaponService: WeaponService) {}

  onRatingClicked(message: string): void {
    this.pageTitle = 'Weapon List: ' + message;
  }

  performFilter(filterBy: string): IWeapon[] {
    filterBy = filterBy.toLocaleLowerCase();
    return this.weapons.filter((weapon: IWeapon) =>
      weapon.weaponName.toLocaleLowerCase().indexOf(filterBy) !== -1);
  }

  filterByCharacter(character: string): void {
    this.selectedCharacter = character;
    this.filteredWeapons = this.weapons.filter((weapon: IWeapon) =>
      weapon.characterName.toLocaleLowerCase() === character.toLocaleLowerCase());
  }

  clearCharacterFilter(): void {
    this.selectedCharacter = null;
    this.filteredWeapons = this.weapons;
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

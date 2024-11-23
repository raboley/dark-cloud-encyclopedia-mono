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
  selectedCharacters: string[] = [];

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

filterByCharacter(character: string, event: MouseEvent): void {
  if (event.shiftKey) {
    const index = this.selectedCharacters.indexOf(character);
    if (index > -1) {
      this.selectedCharacters.splice(index, 1); // Deselect if already selected
    } else {
      this.selectedCharacters.push(character); // Add to selection
    }
  } else {
    this.selectedCharacters = [character]; // Single selection
  }
  this.applyCharacterFilter();
}

clearCharacterFilter(): void {
  this.selectedCharacters = [];
  this.applyCharacterFilter();
}

applyCharacterFilter(): void {
  if (this.selectedCharacters.length === 0) {
    this.filteredWeapons = this.weapons;
  } else {
    this.filteredWeapons = this.weapons.filter(weapon =>
      this.selectedCharacters.includes(weapon.characterName)
    );
  }
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

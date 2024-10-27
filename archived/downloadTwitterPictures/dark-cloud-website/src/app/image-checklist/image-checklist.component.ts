import { Component, OnInit } from '@angular/core';
import { WeaponService } from '../weapons/weapon.service';
import { IWeapon } from '../weapons/weapon';
import { ImageCheckService } from '../image-check.service';

@Component({
  selector: 'pm-image-checklist',
  templateUrl: './image-checklist.component.html',
  styleUrls: ['./image-checklist.component.css']
})
export class ImageChecklistComponent implements OnInit {
  filteredWeapons: IWeapon[] = [];
  weapons: IWeapon[] = [];
  errorMessage = '';
  _listFilter = '';
  weaponUrlRoot: string = 'https://s3-us-west-2.amazonaws.com/dark-cloud-bucket-dev/weapons/images/';
  weaponUrls//: Array<string>; // = "./api/weapons/images/Toan/choora/Toan_Choora_Stats.jpg";
  weaponUrlTypes = {
    stats: 'Stats.jpg',
    main: 'Main.jpg',
    side1: 'Side1.jpg',
    side2: 'Side2.jpg'
  };
  weapon: IWeapon | undefined;
  

  get listFilter(): string {
    return this._listFilter;
  }
  set listFilter(value: string) {
    this._listFilter = value;
    this.filteredWeapons = this.listFilter ? this.performFilter(this.listFilter) : this.weapons;
  }

  performFilter(filterBy: string): IWeapon[] {
    filterBy = filterBy.toLocaleLowerCase();
    return this.weapons.filter((weapon: IWeapon) =>
      weapon.weaponName.toLocaleLowerCase().indexOf(filterBy) !== -1);
  }

  constructor(private weaponService: WeaponService, private imageCheckService: ImageCheckService) {

  }

  getWeaponUrls(weapon: IWeapon[]){
    this.weaponUrls = []
    for (let weapon of this.filteredWeapons) {
      weapon.weaponImageUrls = []
      for (let key in this.weaponUrlTypes) {
        let weaponUrlType = this.weaponUrlTypes[key];
        let weaponPathName = weapon.weaponName.replace(" ","_")
        let url = `${this.weaponUrlRoot}${weapon.characterName}_${weaponPathName}_${weaponUrlType}`
        this.showUrl(weapon, url)
        weapon.weaponImageUrls.push({


          urlType: weaponUrlType,         
          altText: `${weapon.characterName}_${weaponPathName}_${weaponUrlType}`,
          //imageStatus: this.showUrl(weapon, url),
          url: url
          
        })
      }
    }
  }

  showUrl(thing: any, url: string) {
    return this.imageCheckService.getResponse(url)
    // resp is of type `HttpResponse<Config>`
    .subscribe( resp => {
      // display its headers
      // djisfadf
      const keys = resp.headers.keys();
      thing.headers = keys.map(key =>
        `${key}: ${resp.headers.get(key)}`);
    });
}


  ngOnInit(): void {
    this.weaponService.getWeapons().subscribe(
      weapons => {
        this.weapons = weapons;

        this.filteredWeapons = this.weapons;
        this.getWeaponUrls(this.filteredWeapons);
      },
      error => this.errorMessage = <any>error
    );
  }

}

import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

import { IWeapon } from './weapon';
import { WeaponService } from './weapon.service';

@Component({
  templateUrl: './weapon-detail.component.html',
  styleUrls: ['./weapon-detail.component.css']
})
export class WeaponDetailComponent implements OnInit {
  pageTitle = 'Weapon Detail';
  errorMessage = '';6
  weapon: IWeapon | undefined;
  weaponUrl: string;
  weaponUrlRoot: string = './api/weapons/images/';
  //weaponUrlRoot: string = 'https://s3-us-west-2.amazonaws.com/dark-cloud-bucket-dev/weapons/images/';
  weaponUrls//: Array<string>; // = "./api/weapons/images/Toan/choora/Toan_Choora_Stats.jpg";
  weaponUrlTypes = {
    stats: 'Stats.jpg',
    main: 'Main.jpg',
    side1: 'Side1.jpg',
    side2: 'Side2.jpg'
  };

  constructor(private route: ActivatedRoute,
    private router: Router,
    private weaponService: WeaponService) {
  }

  ngOnInit() {
    const param = this.route.snapshot.paramMap.get('id');
    if (param) {
      const id = +param;
      this.getWeapon(id);
      //this.getWeaponUrls(this.weapon.weaponName)
    }
  }

  getWeapon(id: number) {
    this.weaponService.getWeapon(id).subscribe(
      weapon => {
        this.weapon = weapon;
        this.getWeaponUrls(weapon);
      },
      error => this.errorMessage = <any>error);
  }

  getWeaponUrls(weapon: IWeapon){
    this.weaponUrls = []
        for (let key in this.weaponUrlTypes) {
          let weaponUrlType = this.weaponUrlTypes[key];
          let weaponPathName = this.weapon.weaponName.replace(" ","_").replace(" ", "_");
          this.weaponUrls.push({
                        
            url: `${this.weaponUrlRoot}${this.weapon.characterName}_${weaponPathName}_${weaponUrlType}`,
            altText: `${this.weapon.characterName}_${weaponPathName}_${weaponUrlType}`
          })
    }
  }

  onBack(): void {
    this.router.navigate(['/weapons']);
  }

}

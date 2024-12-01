import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { IWeapon } from './weapon';
import { WeaponService } from './weapon.service';
import { ImageModalComponent } from '../image-modal/image-modal.component';

@Component({
  selector: 'pm-weapon-detail',
  templateUrl: './weapon-detail.component.html',
  styleUrls: ['./weapon-detail.component.css']
})
export class WeaponDetailComponent implements OnInit {
  @ViewChild('imageModal') imageModal: ImageModalComponent;
  pageTitle = 'Weapon Detail';
  errorMessage = '';
  weapon: IWeapon | undefined;
  weaponUrl: string;
  weaponUrlRoot = './api/weapons/images/';
  weaponUrls: Array<{url: string, altText: string}>;
  weaponUrlTypes = {
    stats: 'Stats.jpg',
    main: 'Main.jpg',
    side1: 'Side1.jpg',
    side2: 'Side2.jpg'
  };

  constructor(private route: ActivatedRoute,
              private router: Router,
              private weaponService: WeaponService) { }

ngOnInit() {
  this.route.paramMap.subscribe(params => {
    const id = +params.get('id');
    if (id) {
      this.getWeapon(id);
    }
  });
}

goToPreviousWeapon(): void {
  if (this.weapon) {
    const previousWeaponId = this.weaponService.getPreviousWeaponId(this.weapon.weaponId);
    if (previousWeaponId !== null) {
      this.router.navigate(['/weapons', previousWeaponId]);
    }
  }
}
  goToNextWeapon(): void {
  if (this.weapon) {
    console.log('Current weapon:', this.weapon);
    const nextWeaponId = this.weaponService.getNextWeaponId(this.weapon.weaponId);
    console.log('Next weapon ID:', nextWeaponId);
    if (nextWeaponId !== null) {
      this.router.navigate(['/weapons', nextWeaponId]);
    }
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

  getWeaponUrls(weapon: IWeapon) {
    this.weaponUrls = [];
    for (const key in this.weaponUrlTypes) {
      const weaponUrlType = this.weaponUrlTypes[key];
      const weaponPathName = this.weapon.weaponName.replace(' ', '_').replace(' ', '_');
      this.weaponUrls.push({
        url: `${this.weaponUrlRoot}${this.weapon.characterName}_${weaponPathName}_${weaponUrlType}`,
        altText: `${this.weapon.characterName}_${weaponPathName}_${weaponUrlType}`
      });
    }
  }

  openModal(url: string, altText: string) {
    this.imageModal.imageUrl = url;
    this.imageModal.altText = altText;
    this.imageModal.openModal();
  }

  onBack(): void {
    this.router.navigate(['/weapons']);
  }
}

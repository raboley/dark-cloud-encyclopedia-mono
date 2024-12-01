import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, tap, map } from 'rxjs/operators';

import { IWeapon } from './weapon';

@Injectable({
  providedIn: 'root'
})
export class WeaponService {
  private weaponUrl = 'api/weapons/weapons.json';
  private weapons: IWeapon[] = [];

  constructor(private http: HttpClient) { }

  getWeapons(): Observable<IWeapon[]> {
    return this.http.get<IWeapon[]>(this.weaponUrl).pipe(
      tap(data => this.weapons = data), // Store the weapons
      catchError(this.handleError)
    );
  }

  getWeapon(id: number): Observable<IWeapon | undefined> {
    return this.getWeapons().pipe(
      map((weapons: IWeapon[]) => weapons.find(p => p.weaponId === id)),
    );
  }

  getNextWeaponId(currentWeaponId: number): number | null {
    const currentIndex = this.weapons.findIndex(weapon => weapon.weaponId === currentWeaponId);
    if (currentIndex !== -1 && currentIndex < this.weapons.length - 1) {
      return this.weapons[currentIndex + 1].weaponId;
    }
    return null;
  }

  getPreviousWeaponId(currentWeaponId: number): number | null {
  const currentIndex = this.weapons.findIndex(weapon => weapon.weaponId === currentWeaponId);
  if (currentIndex > 0) {
    return this.weapons[currentIndex - 1].weaponId;
  }
  return null;
}

  private handleError(err: HttpErrorResponse) {
    let errorMessage = '';
    if (err.error instanceof ErrorEvent) {
      errorMessage = `An error occurred: ${err.error.message}`;
    } else {
      errorMessage = `Server returned code: ${err.status}, error message is: ${err.message}`;
    }
    console.error(errorMessage);
    return throwError(errorMessage);
  }
}

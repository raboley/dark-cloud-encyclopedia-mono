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

  constructor(private http: HttpClient) { }

  getWeapons(): Observable<IWeapon[]> {
    return this.http.get<IWeapon[]>(this.weaponUrl).pipe(
      
     // tap(data => console.log('All: ' + JSON.stringify(data))),
      catchError(this.handleError)
    );
  }

  getWeapon(id: number): Observable<IWeapon | undefined> {
    return this.getWeapons().pipe(
      map((weapons: IWeapon[]) => weapons.find(p => p.weaponId === id)),
    );
  }

  private handleError(err: HttpErrorResponse) {
    // in a real world app, we may send the server to some remote logging infrastructure
    // instead of just logging it to the console
    let errorMessage = '';
    if (err.error instanceof ErrorEvent) {
      // A client-side or network error occurred. Handle it accordingly.
      errorMessage = `An error occurred: ${err.error.message}`;
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong,
      errorMessage = `Server returned code: ${err.status}, error message is: ${err.message}`;
    }
    console.error(errorMessage);
    return throwError(errorMessage);
  }
}

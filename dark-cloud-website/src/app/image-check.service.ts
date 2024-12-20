import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpResponse } from '@angular/common/http';
import { throwError, Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ImageCheckService {

  constructor(private http: HttpClient) { }

  public getImage(url: string) {
    return this.http.get(url)
    // .pipe(
    //   catchError(this.handleError)
    //)
    ;
  }
  public getResponse(url: string): Observable<HttpResponse<Blob>> {
    return this.http.get(
      url, { observe: 'response', responseType: 'blob' });
  }
  private handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      // A client-side or network error occurred. Handle it accordingly.
      console.error('An error occurred:', error.error.message);
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong,
      console.error(
        `Backend returned code ${error.status}, ` +
        `body was: ${error.error}`);
    }
    // return an observable with a user-facing error message
    // return throwError(
    //   'Something bad happened; please try again later.');
    return 'error triggered'
  };
}

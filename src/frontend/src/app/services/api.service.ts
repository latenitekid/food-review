import { HttpClient } from '@angular/common/http';
import { Injectable, Signal } from '@angular/core';
import { environment } from '../../environments/environment';
import { NewReviewDetails, ReviewDetails } from '../models/review-details';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  constructor(private http: HttpClient) {}

  private get<T>(urlPath: string): Observable<T> {
    const url = `${environment.apiBaseUrl}/${urlPath}`;
    return this.http.get<T>(url);
  }

  private post<T>(urlPath: string, body: any): Observable<T> {
    const url = `${environment.apiBaseUrl}/${urlPath}`;
    return this.http.post<T>(url, body);
  }

  private put<T>(urlPath: string, body: any): Observable<T> {
    const url = `${environment.apiBaseUrl}/${urlPath}`;
    return this.http.put<T>(url, body);
  }

  getLatestReviews(): Observable<ReviewDetails[]> {
    return this.get<ReviewDetails[]>('latest-reviews');
  }

  submitNewReview(reviewDetails: NewReviewDetails): Observable<any> {
    return this.post<any>('new-review', reviewDetails);
  }

  handleCallback(): Observable<any> {
    return this.put<any>('user/login', undefined);
  }
}

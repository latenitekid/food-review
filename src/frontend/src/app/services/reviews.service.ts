import { Injectable } from '@angular/core';
import { ApiService } from './api.service';
import { NewReviewDetails } from '../models/review-details';

@Injectable({
  providedIn: 'root',
})
export class ReviewsService {
  constructor(private apiService: ApiService) {}

  getLatestReviews() {
    return this.apiService.getLatestReviews();
  }

  submitNewReview(reviewDetails: NewReviewDetails) {
    return this.apiService.submitNewReview(reviewDetails);
  }
}

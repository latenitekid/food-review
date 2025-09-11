import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ReviewCardComponent } from "../review-card/review-card.component";
import { NewReviewDetails } from '../../models/review-details';
import { FormsModule } from '@angular/forms';
import { ReviewsService } from '../../services/reviews.service';

@Component({
  selector: 'app-write-a-review',
  standalone: true,
  imports: [ CommonModule, ReviewCardComponent, FormsModule ],
  templateUrl: './write-a-review.component.html',
  styleUrls: ['./write-a-review.component.css']
})
export class WriteAReviewComponent implements OnInit {

  ratingBurgers: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  hoveredBurger: number = 0;
  newReviewDetails: NewReviewDetails;

  constructor(private reviewsService: ReviewsService) {
    this.newReviewDetails = {
      restaurantName: "",
      headline: "",
      mealItems: "",
      mealCost: 0,
      reviewText: "",
      burgerRating: 0,
      reviewDate: new Date(),
      userId: 1
    };
  }

  ngOnInit() {
  }

  getRatingBurgerClass(index: number): string {
    const ratingToCheck = this.hoveredBurger || this.newReviewDetails.burgerRating;
    return ratingToCheck >= index ? "rating-burger-active" : "rating-burger-inactive";
  }

  submitReview(): void {
    this.reviewsService.submitNewReview(this.newReviewDetails).subscribe({
      next: (response) => {
        console.log('Review submitted successfully:', response);
      },
      error: (error) => {
        console.error('Error submitting review:', error);
      }
    });
  }
}

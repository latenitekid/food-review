import { Component, OnInit, Signal, signal } from '@angular/core';
import { ReviewsService } from '../../services/reviews.service';
import { ReviewDetails } from '../../models/review-details';
import { CommonModule } from '@angular/common';
import { ReviewCardComponent } from '../review-card/review-card.component';

@Component({
  selector: 'app-home',
  standalone: true,
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  imports: [ CommonModule, ReviewCardComponent ]
})
export class HomeComponent implements OnInit {
  reviews = signal<ReviewDetails[]>([]);

  constructor(private reviewsService: ReviewsService) { }

  ngOnInit() {
    this.reviewsService.getLatestReviews().subscribe(reviews => {
      this.reviews.set(reviews);
    });
  }

}

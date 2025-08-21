import { Component, Input, OnInit } from '@angular/core';
import { NewReviewDetails, ReviewDetails } from '../../models/review-details';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-review-card',
  standalone: true,
  imports: [ CommonModule ],
  templateUrl: './review-card.component.html',
  styleUrls: ['./review-card.component.css']
})
export class ReviewCardComponent implements OnInit {

  @Input()
  reviewDetails?: NewReviewDetails | ReviewDetails;

  constructor() { }

  ngOnInit() {
  }

}

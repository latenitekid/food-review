import { Component, OnInit } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-your-reviews',
  standalone: true,
  imports: [ RouterLink, RouterLinkActive],
  templateUrl: './your-reviews.component.html',
  styleUrls: ['./your-reviews.component.css']
})
export class YourReviewsComponent implements OnInit {
  constructor() { }

  ngOnInit() {
  }
}

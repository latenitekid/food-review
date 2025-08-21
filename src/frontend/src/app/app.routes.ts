import { Routes } from '@angular/router';
import { AboutComponent } from './components/about/about.component';
import { YourReviewsComponent } from './components/your-reviews/your-reviews.component';
import { WriteAReviewComponent } from './components/write-a-review/write-a-review.component';

export const routes: Routes = [
  { path: 'about', component: AboutComponent },
  { path: 'your-reviews', component: YourReviewsComponent },
  { path: 'write-a-review', component: WriteAReviewComponent },
  { path: '**', redirectTo: '' }
];

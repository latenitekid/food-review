import { Routes } from '@angular/router';
import { AboutComponent } from './components/about/about.component';
import { YourReviewsComponent } from './components/your-reviews/your-reviews.component';
import { WriteAReviewComponent } from './components/write-a-review/write-a-review.component';
import { HomeComponent } from './components/home/home.component';
import { AuthCallbackComponent } from './components/auth-callback/auth-callback.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'your-reviews', component: YourReviewsComponent },
  { path: 'write-a-review', component: WriteAReviewComponent },
  { path: 'callback', component: AuthCallbackComponent },
  { path: '**', redirectTo: '' }
];

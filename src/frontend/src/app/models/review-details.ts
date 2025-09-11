export interface NewReviewDetails {
  userId: number;
  restaurantName: string;
  headline: string;
  burgerRating: number;
  reviewDate: Date;
  mealItems?: string;
  mealCost?: number;
  reviewText: string;
}


export interface ReviewDetails extends NewReviewDetails {
  id: number;
}

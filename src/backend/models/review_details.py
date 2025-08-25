from datetime import date
from pydantic import BaseModel, Field

class NewReviewDetails(BaseModel):
  user_id: int = Field(alias='userId')
  restaurant_name: str = Field(alias='restaurantName')
  headline: str = Field(alias='headline')
  burger_rating: int = Field(alias='burgerRating')
  review_date: date = Field(alias='date')
  meal_items: str = Field(alias='mealItems')
  meal_cost: float = Field(alias='mealCost')
  review_text: str = Field(alias='reviewText')

class ReviewDetails(NewReviewDetails):
  id: int = Field(alias='id')
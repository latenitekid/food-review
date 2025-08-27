from datetime import date
from pydantic import BaseModel
from .model_utils import to_camel

class NewReviewDetails(BaseModel):
  class Config:
    validate_by_name = True
    alias_generator = to_camel

  user_id: int
  restaurant_name: str
  headline: str
  burger_rating: int
  review_date: date
  meal_items: str
  meal_cost: float
  review_text: str

class ReviewDetails(NewReviewDetails):
  class Config:
    validate_by_name = True
    alias_generator = to_camel

  id: int
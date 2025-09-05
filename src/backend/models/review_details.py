from datetime import date
from pydantic import BaseModel
from .model_utils import to_camel

class NewReviewDetails(BaseModel):
  class Config:
    validate_by_name = True
    alias_generator = to_camel

  user_id: int
  movie_name: str
  theater: str
  headline: str
  rating: int
  review_date: date
  review_text: str

class ReviewDetails(NewReviewDetails):
  class Config:
    validate_by_name = True
    alias_generator = to_camel

  id: int
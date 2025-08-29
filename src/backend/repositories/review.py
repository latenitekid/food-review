from configs.config_utils import get_postgres_server_details
from models.review_details import NewReviewDetails, ReviewDetails
from sqlalchemy import create_engine, text

postgres_details = get_postgres_server_details("../../config")
  
engine  = create_engine(f"postgresql://{postgres_details['username']}:{postgres_details['password']}@{postgres_details['host']}:{postgres_details['port']}/foodreview")

def add_new_review(review: NewReviewDetails):
  with engine.connect() as conn:
    conn.execute(
      text("""
        INSERT INTO reviews
          (user_id, restaurant_name, headline,
          rating, date, meal_items, meal_cost,
          review_text)
        VALUES
          (1, :restaurant_name, :headline,
          :rating, :date, :meal_items, :meal_cost,
          :review_text)
        """
          ),
        {
          "restaurant_name": review.restaurant_name,
          "headline": review.headline,
          "rating": review.burger_rating,
          "date": review.review_date,
          "meal_items": review.meal_items,
          "meal_cost": review.meal_cost,
          "review_text": review.review_text
        }
    )

    conn.commit()

def get_latest_reviews(limit: int = 5) -> list[ReviewDetails]:
  with engine.connect() as conn:
    result = conn.execute(
      text("""
          SELECT id, user_id, restaurant_name , headline,
            rating as burger_rating, date as review_date, meal_items, meal_cost, review_text
          FROM reviews
          ORDER BY created_at DESC
          LIMIT :limit
          """),
          {
            "limit": limit
          }
    )

    return [ReviewDetails(**row) for row in result.mappings()]
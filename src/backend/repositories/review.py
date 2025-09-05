from models.review_details import NewReviewDetails, ReviewDetails
from sqlalchemy import create_engine, text

engine  = create_engine("postgresql://foodreview:password@localhost:9999/foodreview")

def add_new_review(review: NewReviewDetails):
  with engine.connect() as conn:
    conn.execute(
      text("""
        INSERT INTO reviews
          (user_id, movie_name, theater, headline,
          rating, date, review_text)
        VALUES
          (1, :movie_name, :theater, :headline,
          :rating, :date, :review_text)
        """
          ),
        {
          "movie_name": review.movie_name,
          "theater": review.theater,
          "headline": review.headline,
          "rating": review.rating,
          "date": review.review_date,
          "review_text": review.review_text
        }
    )

    conn.commit()

def get_latest_reviews(limit: int = 5) -> list[ReviewDetails]:
  with engine.connect() as conn:
    result = conn.execute(
      text("""
          SELECT id, user_id, movie_name, headline,
            rating, date as review_date, review_text
          FROM reviews
          ORDER BY created_at DESC
          LIMIT :limit
          """),
          {
            "limit": limit
          }
    )

    return [ReviewDetails(**row) for row in result.mappings()]
from configs.config_utils import get_postgres_server_details
from models.review_details import NewReviewDetails, ReviewDetails
from sqlalchemy import create_engine, text

postgres_details = get_postgres_server_details("../../config")
  
engine  = create_engine(f"postgresql://{postgres_details['username']}:{postgres_details['password']}@{postgres_details['host']}:{postgres_details['port']}/foodreview")

# These functions should have ground truth on these items but the query parameters need to set the defaults at run-time
DEFAULT_REVIEW_LIMIT = 5
DEFAULT_USER_ID = -1
DEFAULT_RESTAURANT_NAME = ""

# ADDING REVIEWS
def add_new_review(review: NewReviewDetails):
  with engine.connect() as conn:
    conn.execute(
      text("""
        INSERT INTO reviews
          (user_id, restaurant_name, headline,
          rating, date, meal_items, meal_cost,
          review_text)
        VALUES
          (:user_id, :restaurant_name, :headline,
          :rating, :date, :meal_items, :meal_cost,
          :review_text)
        """
          ),
        {
          "user_id": review.user_id,
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

# GETTING REVIEWS
## LATEST REVIEWS
def get_latest_reviews(limit: int, user_id: int, restaurant_name: str) -> list[ReviewDetails]:
  # If user_id is provided, remove it from the columns returned? Same for restaurant_name?
  query_string = """
    SELECT id,
      user_id,
      restaurant_name,
      headline,
      rating as burger_rating,
      date as review_date,
      meal_items,
      meal_cost,
      review_text
    FROM reviews
    """
    
  where_clauses = []
  if(restaurant_name != DEFAULT_RESTAURANT_NAME):
    where_clauses.append("restaurant_name = :restaurant_name")
  if(user_id > 0):
    where_clauses.append("user_id = :user_id")
  query_string += craft_where_clause(where_clauses)
  
  query_string += """
    ORDER BY created_at DESC
    LIMIT :limit
    """
  
  with engine.connect() as conn:
    result = conn.execute(
      text(query_string),
          {
            "limit": limit,
            "user_id": user_id,
            "restaurant_name": restaurant_name
          }
    )

    return [ReviewDetails(**row) for row in result.mappings()]

## BEST REVIEWS    
def get_best_reviews(limit: int = DEFAULT_REVIEW_LIMIT, user_id: int = -1, restaurant_name: str = ""):
  # If user_id is provided, remove it from the columns returned? Same for restaurant_name
  query_string = """
    SELECT id,
      user_id,
      restaurant_name,
      headline,
      rating as burger_rating,
      date as review_date,
      meal_items,
      meal_cost,
      review_text
    FROM reviews
    """

  where_clauses = []
  if(restaurant_name != DEFAULT_RESTAURANT_NAME):
    where_clauses.append("restaurant_name = :restaurant_name")
  if(user_id > 0):
    where_clauses.append("user_id = :user_id")
  query_string += craft_where_clause(where_clauses)
  
  query_string += """
    ORDER BY rating DESC
    LIMIT :limit
    """
  
  with engine.connect() as conn:
    result = conn.execute(
      text(query_string),
          {
            "limit": limit,
            "user_id": user_id,
            "restaurant_name": restaurant_name
          }
    )
    
    return [ReviewDetails(**row) for row in result.mappings()]
  
def craft_where_clause(clauses):
  if not clauses:
    return ""
  
  conditions = " AND ".join(clauses)
  return f"WHERE {conditions}"
from models.review_details import NewReviewDetails, ReviewDetails
import repositories.review
from repositories.review import DEFAULT_RESTAURANT_NAME, DEFAULT_REVIEW_LIMIT, DEFAULT_USER_ID
import repositories.user
from fastapi import APIRouter, FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
import uvicorn

app = FastAPI()
router = APIRouter()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@router.post("/new-review")
async def post_new_review(new_review_details: NewReviewDetails):
  repositories.review.add_new_review(new_review_details)
  return {"test": f"thx for the review about {new_review_details.restaurant_name}"}

@router.get("/latest-reviews")
async def get_latest_reviews(limit: int = repositories.review.DEFAULT_REVIEW_LIMIT, user_id: int = DEFAULT_USER_ID, restaurant_name: str = DEFAULT_RESTAURANT_NAME) -> list[ReviewDetails]:
  latest_reviews = repositories.review.get_latest_reviews(limit, user_id, restaurant_name)
  return latest_reviews

@router.get("/best-reviews")
async def get_best_reviews(limit: int = repositories.review.DEFAULT_REVIEW_LIMIT, user_id: int = DEFAULT_USER_ID, restaurant_name: str = DEFAULT_RESTAURANT_NAME) -> list[ReviewDetails]:
  best_reviews = repositories.review.get_best_reviews(limit, user_id, restaurant_name)
  return best_reviews

@router.put("/user/login")
async def put_user(authorization: Annotated[str | None, Header()] = None):
  user_added = repositories.user.add_user(authorization)
  return user_added

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
from models.review_details import NewReviewDetails, ReviewDetails
import repositories.review
from fastapi import APIRouter, FastAPI
import uvicorn

app = FastAPI()
router = APIRouter()

@router.post("/new-review")
async def post_new_review(new_review_details: NewReviewDetails):
  repositories.review.add_new_review(new_review_details)
  return {"test": f"thx for the review about {new_review_details.movie_name}"}

@router.get("/latest-reviews")
async def get_latest_reviews() -> list[ReviewDetails]:
  latest_reviews = repositories.review.get_latest_reviews()
  return latest_reviews

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
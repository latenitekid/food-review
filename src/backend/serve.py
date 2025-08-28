from models.review_details import NewReviewDetails, ReviewDetails
import repositories.review
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
async def get_latest_reviews() -> list[ReviewDetails]:
  latest_reviews = repositories.review.get_latest_reviews()
  return latest_reviews

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import APIRouter

import models
import database as db

router = APIRouter(tags=["reviews"])


@router.get("/reviews")
async def get_reviews():
    return db.read_reviews()


@router.post("/reviews")
async def create_review(reviews: models.Review):
    return db.create_review(reviews)
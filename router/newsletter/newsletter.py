from fastapi import APIRouter

import models
import database as db

router = APIRouter(tags=["newsletter"])

@router.get("/newsletter")
async def get_newsletter():
    return db.read_newsletter()


@router.post("/newsletter")
async def create_newsletter(newsletter: models.Newsletter):
    return db.create_newsletter(newsletter)

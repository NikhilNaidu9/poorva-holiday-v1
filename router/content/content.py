from fastapi import APIRouter

import models
import database as db

router = APIRouter(tags=["content"])


@router.get("/content/{category}")
async def get_content(category: str):
    output = db.read_content(category)
    output[0]['data'] = db.manipulate_load(output[0]['data'])
    return output[0]


@router.post("/content")
async def create_content(content: models.Content):
    return db.create_content(content)

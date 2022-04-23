from fastapi import APIRouter

import models
import database as db

router = APIRouter(tags=["contact us"])


@router.post("/contact")
async def create_contact(contact: models.Contact):
    return db.create_contact(contact)


@router.get("/contact")
async def get_contact():
    return db.read_contact()
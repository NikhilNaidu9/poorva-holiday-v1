from fastapi import APIRouter

import models

router = APIRouter(tags=["cruise"])

cruises = []


@router.post("/cruise")
async def create_cruise(cruise: models.Cruise):
    cruises.append(cruise)
    return "created"


@router.get("/cruise")
async def get_cruise():
    return cruises

from fastapi import APIRouter

import models

router = APIRouter(tags=["flights"])

flights = []


@router.post("/flight")
async def create_flight(flight: models.Flight):
    flights.append(flight)
    return "created"


@router.get("/flight")
async def get_flight():
    return flights

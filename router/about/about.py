from typing import List
from fastapi import APIRouter

router = APIRouter(tags=["services"])

about = [
    {
        "name": "Owner",
        "description":"Poorva Holidays is one of the prestigious travel management company who is specialized in organizing tours to Leh Ladakh, since past 9 years. Mr. Tejas Shah, proprietor of Poorva Holidays has put in all his efforts over the years, to develop networks and proper management facilities at locations where he organizes and offers tours to, for his clients to have better memories to take back home.\n\nA long run in this field has taught us a lot, and hence, we have evolved as one of the best travel experience delivering organization. We believe in delivering convenience and premium experience, to our clients while they are over their tour, as we strive hard to make it their special memory for life."
    },
    {
        "name": "Company",
        "description":"Poorva Holidays is one of the prestigious travel management company who is specialized in organizing tours to Leh Ladakh, since past 9 years. Mr. Tejas Shah, proprietor of Poorva Holidays has put in all his efforts over the years, to develop networks and proper management facilities at locations where he organizes and offers tours to, for his clients to have better memories to take back home.\n\nA long run in this field has taught us a lot, and hence, we have evolved as one of the best travel experience delivering organization. We believe in delivering convenience and premium experience, to our clients while they are over their tour, as we strive hard to make it their special memory for life."
    }
]

@router.get("/about")
async def get_about():
    return about


@router.post("/about")
async def create_about(about: List[dict]):
    return about
from fastapi import APIRouter

import models

router = APIRouter(tags=["config"])

t_c = ["If the Guest decides to cancel the tour for any reason whatsoever then he/she shall give a written application to the company within specified time limit along with original receipt issued by the Company. Such cancellatin will attract Cancellation charges stated hereunder.", "Cancellation charges will be calculated on gross tour cost and the cancellation charges shall depend on date of departure and date of cancellation.","Cancellation charges for any type of transport ticket are applicable as per the rules of the concerned authority.", "Air tickets issued on special fares are NON REFUNDABLE and Guest shall bear cancellation charges.", "Any refund payable to the Guest will be paid after the Company recieves refund from the respective authorities. The Company deducts processing charges from the refund to be paid to Guest."]
contact = []


@router.get("/config")
async def get_config():
    return {"T&C": t_c, "Contact": contact}


@router.post("/tc")
async def create_tc(term: models.Term):
    return "created"

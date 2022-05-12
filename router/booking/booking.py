from fastapi import APIRouter
from typing import List
import uuid

import models
import database as db

router = APIRouter(tags=["booking"])


@router.get("/booking/{user_id}")
async def get_booking(user_id: str):
    outputs = db.read_booking(user_id)
    arr = []
    if outputs != None:
        for output in outputs:
            output['booking_guest_details'] = db.manipulate_load(
                output['booking_guest_details'])
            arr.append(output)

    return arr


@router.get("/admin/booking/total")
async def read_total_booking():
    outputs = db.read_total_booking()
    return outputs


@router.get("/admin/booking/package/total")
async def read_total_package_booking():
    outputs = db.read_total_package_booking()
    return outputs


@router.get("/admin/booking/package")
async def read_booking_by_package_id(package_id: str):
    outputs = db.read_booking_by_package_id(package_id)

    result = []

    for output in outputs:
        
        output['booking_guest_details'] = db.manipulate_load(output['booking_guest_details'])[0]

        result.append(output)

    return result


@router.post("/booking")
async def create_booking(booking: models.Booking):
    booking_id = uuid.uuid4()
    db.create_booking(booking, booking_id)

    return {
        "booking_id": str(booking_id)
    }


@router.patch("/booking/{booking_id}")
async def update_booking(booking_id: str, update_list: list):

    for i in range(len(update_list)):
        data = db.update_booking(
            booking_id, update_list[i]["key"], update_list[i]["value"])

    return data


@router.delete("/booking/{booking_id}")
async def delete_booking(booking_id):
    return db.delete_booking(booking_id)

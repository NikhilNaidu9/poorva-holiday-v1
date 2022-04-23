from fastapi import APIRouter

import models
import database as db

router = APIRouter(tags=["staff"])

staffs = []


@router.post("/staff")
async def create_staff(staff: models.Staff):
    return db.create_staff(staff)


@router.get("/staff/{staff_id}")
async def get_staff(staff_id):
    return db.read_staff(staff_id)


@router.patch("/staff/{staff_id}")
async def update_staff(staff_id, update_list: list):

    for i in range(len(update_list)):
        data = db.update_staff(
            staff_id, update_list[i]["key"], update_list[i]["value"])
    return data


@router.delete("/staff/{staff_id}")
async def delete_staff(staff_id):
    return db.delete_staff(staff_id)

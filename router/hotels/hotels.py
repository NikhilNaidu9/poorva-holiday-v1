from fastapi import APIRouter
from typing import List

import models
import database as db

router = APIRouter(tags=["hotels"])

hotels = []


@router.post("/hotel")
async def create_hotel(hotel: models.Hotel):
    hotels.append(hotel)
    return db.create_hotel(hotel)


@router.get("/hotel/all")
async def get_all_hotel():
    
    arr =[]
    out = db.read_all_hotel()
    
    for output in out:
        output['hotel_review'] = db.manipulate_load(output['hotel_review'])
        output['hotel_rooms'] = db.manipulate_load(output['hotel_rooms'])
        output['hotel_offer'] = db.manipulate_load(output['hotel_offer'])
        output['hotel_gallery_link'] = db.manipulate_load(output['hotel_gallery_link'])
        output['hotel_landmarks'] = db.manipulate_load(output['hotel_landmarks'])
        output['hotel_availability'] = db.manipulate_load(output['hotel_availability'])
        output['hotel_amenities'] = db.manipulate_load(output['hotel_amenities'])
        arr.append(output)
    
    return arr


@router.get("/hotel/{hotel_id}")
async def get_hotel(hotel_id: str):
    output = db.read_hotel(hotel_id)
    if output != None:
        output['hotel_review'] = db.manipulate_load(output['hotel_review'])
        output['hotel_rooms'] = db.manipulate_load(output['hotel_rooms'])
        output['hotel_offer'] = db.manipulate_load(output['hotel_offer'])
        output['hotel_gallery_link'] = db.manipulate_load(output['hotel_gallery_link'])
        output['hotel_landmarks'] = db.manipulate_load(output['hotel_landmarks'])
        output['hotel_availability'] = db.manipulate_load(output['hotel_availability'])
        output['hotel_amenities'] = db.manipulate_load(output['hotel_amenities'])
    return output


@router.patch("/hotel/{hotel_id}")
async def update_staff(hotel_id: str, update_list: list):
    
    for i in range(len(update_list)):
        data = db.update_hotel(hotel_id, update_list[i]["key"], update_list[i]["value"])
    
    return data


@router.delete("/hotel/{hotel_id}")
async def delete_hotel(hotel_id):
    return db.delete_hotel(hotel_id)
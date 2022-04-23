from fastapi import APIRouter
from typing import List

import models
import database as db

router = APIRouter(tags=["package"])


@router.post("/package")    
async def create_package(package: models.Package):
    return db.create_package(package)


@router.get("/package/all")
async def get_all_packages():
    
    arr =[]
    out = db.read_all_package()
    
    for output in out:
        output['package_offers'] = db.manipulate_load(output['package_offers'])
        output['package_theme'] = db.manipulate_load(output['package_theme'])
        output['package_gallery_link'] = db.manipulate_load(output['package_gallery_link'])
        output['package_hotel'] = db.manipulate_load(output['package_hotel'])
        output['package_flight'] = db.manipulate_load(output['package_flight'])
        output['package_cruise'] = db.manipulate_load(output['package_cruise'])
        output['package_activities'] = db.manipulate_load(output['package_activities'])
        output['package_availability'] = db.manipulate_load(output['package_availability'])
        output['day_activites'] = db.manipulate_load(output['day_activites'])
        output['itenary_inclusion'] = db.manipulate_load(output['itenary_inclusion'])
        output['itenary_exclusion'] = db.manipulate_load(output['itenary_exclusion'])
        output['package_cost'] = db.manipulate_load(output['package_cost'])
        output['package_cancellation_policy'] = db.manipulate_load(output['package_cancellation_policy'])
        output['package_stay'] = db.manipulate_load(output['package_stay'])
        arr.append(output)
    
    return arr


@router.get("/package/{package_id}")
async def get_package(package_id: str):
    output = db.read_package(package_id)
    if output != None:
        output['package_offers'] = db.manipulate_load(output['package_offers'])
        output['package_theme'] = db.manipulate_load(output['package_theme'])
        output['package_gallery_link'] = db.manipulate_load(output['package_gallery_link'])
        output['package_hotel'] = db.manipulate_load(output['package_hotel'])
        output['package_flight'] = db.manipulate_load(output['package_flight'])
        output['package_cruise'] = db.manipulate_load(output['package_cruise'])
        output['package_activities'] = db.manipulate_load(output['package_activities'])
        output['package_availability'] = db.manipulate_load(output['package_availability'])
        output['day_activites'] = db.manipulate_load(output['day_activites'])
        output['itenary_inclusion'] = db.manipulate_load(output['itenary_inclusion'])
        output['itenary_exclusion'] = db.manipulate_load(output['itenary_exclusion'])
        output['package_cost'] = db.manipulate_load(output['package_cost'])
        output['package_cancellation_policy'] = db.manipulate_load(output['package_cancellation_policy'])
        output['package_stay'] = db.manipulate_load(output['package_stay'])
    return output


@router.patch("/package/{package_id}")
async def update_package(package_id: str, update_list: list):
    
    for i in range(len(update_list)):
        data = db.update_package(package_id, update_list[i]["key"], update_list[i]["value"])
    
    return data


@router.delete("/package/{package_id}")
async def delete_package(package_id):
    return db.delete_package(package_id)
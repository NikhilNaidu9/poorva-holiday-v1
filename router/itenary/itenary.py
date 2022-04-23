from fastapi import APIRouter

import models
import database as db

router = APIRouter(tags=["itenary"])

@router.post("/itenary")
async def create_itenary(itenary: models.Itenary):
    return db.create_itenary(itenary)


@router.get("/itenary/all")
async def get_all_itenary():
    
    arr =[]
    out = db.read_all_itenary()
    
    for output in out:
        output['day_activites'] = db.manipulate_load(output['day_activites'])
        output['itenary_inclusion'] = db.manipulate_load(output['itenary_inclusion'])
        output['itenary_exclusion'] = db.manipulate_load(output['itenary_exclusion'])
        arr.append(output)
    
    return arr


@router.get("/itenary/{itenary_id}")
async def get_user(itenary_id: str):
    output = db.read_itenary(itenary_id) 
    if output != None:
        output['day_activites'] = db.manipulate_load(output['day_activites'])
        output['itenary_inclusion'] = db.manipulate_load(output['itenary_inclusion'])
        output['itenary_exclusion'] = db.manipulate_load(output['itenary_exclusion'])
    return output


@router.patch("/itenary/{itenary_id}")
async def update_itenary(itenary_id: str, update_list: list):
    
    for i in range(len(update_list)):
        data = db.update_itenary(itenary_id, update_list[i]["key"], json.dumps((update_list[i]["value"])))
    
    return data


@router.delete("/itenary/{itenary_id}")
async def delete_itenary(itenary_id):
    return db.delete_itenary(itenary_id)

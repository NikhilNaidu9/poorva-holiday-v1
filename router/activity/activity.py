from fastapi import APIRouter
import json
import models
import database as db

router = APIRouter(tags=["activity"])


@router.post("/activity")
async def create_activity(activity: models.DayActivity):
    return db.create_activity(activity)


@router.get("/activity/all")
async def get_all_activity():
    
    arr =[]
    out = db.read_all_activity()
    
    for output in out:
        output['plan'] = db.manipulate_load(output['plan'])
        arr.append(output)
    
    return arr


@router.get("/activity/{activity_id}")
async def get_activity(activity_id: str):
    output = db.read_activity(activity_id)
    if output != None:
        output['plan'] = db.manipulate_load(output['plan'])
    return output


@router.patch("/activity/{activity_id}")
async def update_activity(activity_id: str, update_list: list):
    
    for i in range(len(update_list)):
        data = db.update_activity(activity_id, update_list[i]["key"], json.dumps((update_list[i]["value"])))
    
    return data


@router.delete("/activity/{activity_id}")
async def delete_activity(activity_id):
    return db.delete_activity(activity_id)
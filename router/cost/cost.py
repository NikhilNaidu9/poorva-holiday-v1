from fastapi import APIRouter
import json
import models
import database as db

router = APIRouter(tags=["cost"])


@router.post("/cost")
async def create_cost(cost: models.Cost):
    return db.create_cost(cost)


@router.get("/cost/all")
async def get_all_cost():
    
    arr =[]
    out = db.read_all_cost()
    
    for output in out:
        output['cost_plan'] = db.manipulate_load(output['cost_plan'])
        arr.append(output)
    
    return arr


@router.get("/cost/{cost_id}")
async def get_cost(cost_id: str):
    output = db.read_cost(cost_id)
    if output != None:
        output['cost_plan'] = db.manipulate_load(output['cost_plan'])
    return output


@router.patch("/cost/{cost_id}")
async def update_cost(cost_id: str, update_list: list):
    
    for i in range(len(update_list)):
        data = db.update_activity(cost_id, update_list[i]["key"], json.dumps((update_list[i]["value"])))
    
    return data


@router.delete("/cost/{cost_id}")
async def delete_cost(cost_id):
    return db.delete_cost(cost_id)
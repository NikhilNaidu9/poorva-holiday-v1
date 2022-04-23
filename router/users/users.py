from fastapi import APIRouter

import models
import database as db

router = APIRouter(tags=["user"])

users = []


@router.post("/user")
async def create_user(user: models.User):
    users.append(user)
    return db.create_user(user)


@router.get("/user/{user_id}")
async def get_user(user_id):
    return db.read_user(user_id)


@router.patch("/user/{user_id}")
async def update_user(user_id, update_list: list):
    
    for i in range(len(update_list)):
        data = db.update_user(user_id, update_list[i]["key"], update_list[i]["value"])
    return data


@router.delete("/user/{user_id}")
async def delete_user(user_id):
    return db.delete_user(user_id)
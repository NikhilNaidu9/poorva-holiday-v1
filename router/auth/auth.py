import models as models
import authentication as auth
import database as db
from fastapi import APIRouter

router = APIRouter(tags=['authentication'])


@router.post("/auth/signup")
async def sign_up(data: models.Authentication):

    err, data = auth.sign_up(data)

    if err != None:
        return {
            "status": "failure",
            "data": data,
            "error": err
        }
    else:
        return {
            "status": "success",
            "data": data,
            "error": None
        }


@router.post("/auth/login")
async def login(data: models.Authentication):

    err, data = auth.login(data)

    if err != None:
        return {
            "status": "failure",
            "data": data,
            "error": err
        }
    else:
        return {
            "status": "success",
            "data": data,
            "error": None
        }


@router.post("/auth/forget_password")
async def forget_password(data: models.Authentication):

    err, data = auth.forget_password(data)

    if err != None:
        return {
            "status": "failure",
            "data": data,
            "error": err
        }
    else:
        return {
            "status": "success",
            "data": data,
            "error": None
        }


@router.post("/auth/confirm_password")
async def confirm_forget_password(data: models.Authentication):

    err, data = auth.confirm_forget_password(data)

    if err != None:
        return {
            "status": "failure",
            "data": data,
            "error": err
        }
    else:
        return {
            "status": "success",
            "data": data,
            "error": None
        }


@router.post("/auth/admin/login")
async def staff_login(user_id: str, user_password: str):

    return db.staff_login(user_id, user_password)

from fastapi import APIRouter

import models
import database as db

router = APIRouter(tags=["services"])


@router.get("/services")
async def get_services():
    return db.read_services()


@router.post("/services")
async def create_services(service: models.Service):
    return db.create_service(service)


@router.delete("/services/{service_id}")
async def delete_services(service_id: str):
    return db.delete_service(service_id)
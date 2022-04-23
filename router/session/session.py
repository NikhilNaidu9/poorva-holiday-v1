from fastapi import APIRouter

import models
import database as db

router = APIRouter(tags=["session"])


@router.post("/session")
async def create_session(session: models.Session):
    return db.create_session(session.session_id, session.order_id, session.package_id, session.total_price)
    

@router.delete("/session/{session_id}")
async def delete_session(session_id: str):
    return db.delete_session(session_id)


@router.get("/session/{session_id}")
async def read_session(session_id: str):
    return db.read_session(session_id)


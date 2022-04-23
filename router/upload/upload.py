from fastapi import APIRouter, UploadFile, File
import shutil
import database as db

router = APIRouter(tags=["upload"])


@router.post("/upload_image/{purpose}/")
async def image(purpose: str, image: UploadFile = File(...)):

    if image.filename.split(".")[1] == "png":
        with open(f"{purpose}.png", "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        return db.upload_image(f"{purpose}.png", purpose)
    elif (
        image.filename.split(".")[1] == "jpeg" or image.filename.split(".")[1] == "jpg"
    ):
        with open(f"{purpose}.jpeg", "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        return db.upload_image(f"{purpose}.jpeg", purpose)
    else:
        return "Choose PNG or JPEG images only"
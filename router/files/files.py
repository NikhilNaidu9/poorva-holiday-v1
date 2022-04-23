from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from os import getcwd
import shutil

router = APIRouter(tags=["files"])


@router.get("/file/{file_name}")
def get_file(file_name: str):
    return FileResponse(path=getcwd() + "/static/" + file_name + ".pdf")


@router.post("/file/upload/{file_name}", tags=["upload"])
async def image(file_name: str, pdf: UploadFile = File(...)):
    
    with open(getcwd() + f"/static/{file_name}.pdf", "wb") as buffer:
        shutil.copyfileobj(pdf.file, buffer)

    return "file uploaded"
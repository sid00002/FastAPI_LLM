from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def check():
    return {"status":"Ok Working Fine"}
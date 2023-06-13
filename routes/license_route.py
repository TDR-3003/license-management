from fastapi import APIRouter, status, HTTPException, Depends
from models.schemas import Login
from config.token_utils import write_token
from fastapi.responses import JSONResponse
from repositories import AuthRepository
from models.schemas import Users
from config.oauth import get_current_user

license_route = APIRouter()


@license_route.get("/licenses", status_code=status.HTTP_200_OK)
async def get_licenses(current_user: Users = Depends(get_current_user)):
    try:
        print(current_user)
        return "Licenses"
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail={"status": e.status_code, "message": e.detail})

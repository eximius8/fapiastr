from fastapi import APIRouter
from models.dbversion import Versiondb

router = APIRouter()



@router.get("/api/dbversion")
async def get_db_version():
    return {"version": Versiondb.get_version()}

@router.get("/api/incrementdbversion")
async def increment_db_version():
    return {"version": Versiondb.increm(val=1)}


@router.get("/api/derementdbversion")
async def increment_db_version():
    return {"version": Versiondb.increm(val=-1)}
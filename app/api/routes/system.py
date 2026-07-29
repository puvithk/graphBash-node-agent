

# pyrefly: ignore [missing-import]
from fastapi import APIRouter

router  = APIRouter()

@router.get("/health")
def health() :
    return {
        "status" : "Running"
    }

@router.get("/info")
def system_info():
    return {
        "system_name" : "Puvith ubuntu" , 
        "version" : "v1"
    }


@router.get("/uptime")
def system_uptime():
    return{
        "uptime" : ""
    }
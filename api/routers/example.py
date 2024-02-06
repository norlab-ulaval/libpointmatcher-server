from fastapi import APIRouter

router = APIRouter()


# TODO keep only as example for now
@router.get("/example")
def hello_world():
    return {"Hello": "World"}

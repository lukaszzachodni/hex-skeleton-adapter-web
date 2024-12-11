import datetime
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Entity(BaseModel):
    id: int
    message: str
    createdAt: str


class EntityResponse(BaseModel):
    data: Entity


class EntityRequest(BaseModel):
    message: str


@app.get("/entity/{id}", response_model=EntityResponse)
async def get_entity(id: int):
    entity = Entity(
        id=id, message="Example message", createdAt=datetime.datetime.now().isoformat()
    )
    return {"data": entity}


@app.post("/entity", response_model=EntityResponse, status_code=201)
async def create_entity(entity_request: EntityRequest):
    entity = Entity(
        id=1,
        message=entity_request.message,
        createdAt=datetime.datetime.now().isoformat(),
    )
    return {"data": entity}

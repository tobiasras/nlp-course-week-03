import os

from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI()

CAMPUSAI_API_KEY = os.environ.get("CAMPUSAI_API_KEY", "")
CAMPUSAI_MODEL = os.environ.get("CAMPUSAI_MODEL", "")
CAMPUSAI_EMBED_MODEL = os.environ.get("CAMPUSAI_EMBED_MODEL", "")
CAMPUSAI_API_URL = os.environ.get("CAMPUSAI_API_URL", "")


class ExtractPersonsRequest(BaseModel):
    text: str = Field(..., min_length=1)


class ExtractPersonsResponse(BaseModel):
    persons: list[str]


@app.get("/")
async def root():
    return {"message": "app is running good:)"}


@app.post("/v1/extract-persons")
async def extract_persons(req: ExtractPersonsRequest) -> ExtractPersonsResponse:
    return ExtractPersonsResponse(persons=[])


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

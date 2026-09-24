from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uvicorn

from extract import campusai_extract_persons

app = FastAPI()

class ExtractPersonsRequest(BaseModel):
    text: str = Field(..., min_length=1)

class ExtractPersonsResponse(BaseModel):
    persons: list[str]

@app.get("/")
async def root():
    return {"message": "app is running good:)"}

@app.post("/v1/extract-persons", response_model=ExtractPersonsResponse)
async def extract_persons(req: ExtractPersonsRequest):
    try:
        persons = campusai_extract_persons(req.text)
        return ExtractPersonsResponse(persons=persons)
    except ValueError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


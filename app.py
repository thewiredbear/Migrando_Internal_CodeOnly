
from http.client import HTTPException
from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from migrandoLeadScore.entity.request_body import RequestBody
import httpx


text:str = "What is Text Summarization?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")



@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")
    



@app.post("/predict")
async def predict(request_body: RequestBody):
    url = "https://hassanbutt.app.modelbit.com/v1/predict/latest"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=request_body.dict())
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=exc.response.text)
    except httpx.RequestError as exc:
        raise HTTPException(status_code=500, detail=str(exc))

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
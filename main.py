from fastapi import FastAPI
from app.api import health
app = FastAPI(title="schooldb")
app.include_router(health.router)




@app.get("/")
async def root():
    return {"message": "schooldb api is running"}
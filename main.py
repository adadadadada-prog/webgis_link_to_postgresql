from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from fastapi import Request
from app.load_point import store_point
app = FastAPI()

@app.get("/")
async def root():
    return 


@app.get("/aa",response_class=HTMLResponse)
async def root(request : Request):
    
    html_content = open("templates\index.html",encoding="utf-8").read()
    return html_content


@app.post("/post_point",response_class=HTMLResponse)
async def root(request : Request):
    
    form_data = await request.json()
    print(form_data)
    lat = float(form_data["lat"])
    lon = float(form_data["lon"])
    print(lat,lon)
    store_point(lat,lon)
    return "get_point"

if __name__ == "__main__":
    uvicorn.run(app='main:app',reload=True)
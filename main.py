from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from fastapi import Request
from fastapi.templating import Jinja2Templates

from app.s_point import store_point
from app.s_line import store_line
from app.load_data import load_pointdata
from app.load_data import load_line
app = FastAPI()

@app.get("/")
async def root():
    return 

templates = Jinja2Templates(directory="templates")
@app.get("/aa",response_class=HTMLResponse)
async def root(request : Request):
    points = load_pointdata()
    lines = load_line()
    
    
    return templates.TemplateResponse(request=request,name="index.html", context={"points": points,"lines":lines})

@app.post("/post_point",response_class=HTMLResponse)
async def root(request : Request):
    
    form_data = await request.json()
    
    lat = float(form_data["lat"])
    lon = float(form_data["lon"])
    
    store_point(lat,lon)
    return "get_point"

@app.post("/post_line",response_class=HTMLResponse)
async def root(request : Request):
    
    form_data = await request.json()
    print(form_data)
    
    store_line(form_data)
    return "get_point"

@app.post("/post_polygon",response_class=HTMLResponse)
async def root(request : Request):
    
    pass

if __name__ == "__main__":
    uvicorn.run(app='main:app',reload=True)
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
import uvicorn
from fastapi import Request
from fastapi.templating import Jinja2Templates

from app.s_point import store_point
from app.s_line import store_line
from app.s_polygon import store_polygon
from app.load_data import load_pointdata
from app.load_data import load_line
from app.load_data import load_polygon
from fastapi.staticfiles import StaticFiles
from app.match import match_db
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return 

templates = Jinja2Templates(directory="templates")
@app.get("/aa",response_class=HTMLResponse)
async def root(request : Request):
    points = load_pointdata()
    lines = load_line()
    polygons = load_polygon()
    
    
    return templates.TemplateResponse(request=request,name="index.html", context={"points": points,"lines":lines,"polys":polygons})


@app.post("/matchbase",response_class=JSONResponse)
async def root(request : Request):
    form_data = await request.json()
    index = match_db(form_data.get("type"),form_data)
    print(index)
    return index
    

if __name__ == "__main__":
    uvicorn.run(app='main:app',reload=True)
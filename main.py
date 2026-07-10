from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from fastapi import Request
from app import load_point
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
    
    html_content = open("templates\index.html",encoding="utf-8").read()
    form_data = await request.form()
    lat = float(form_data["lat"])
    lon = float(form_data["lon"])
    print(lat,lon)
    load_point(lat,lon)
    return "get_point"

if __name__ == "__main__":
    uvicorn.run(app,reload=True)
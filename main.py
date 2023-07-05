from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from controller import GraphController
from model import BorderModel

app = FastAPI() 

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory = "templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request): 
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/find-path")
def find_path(data: BorderModel): 
    controller = GraphController()
    return controller.get_path(data)
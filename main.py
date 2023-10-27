from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
#from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
name = "Erdal Erdogan"

skills =["Hard- und Software", "Betriebssysteme", "Netzwerke", "Open Source Software", "Cloud Computing", "AWS", "Git", "Python, VSCode, html, css, js, php", "CMS", "Musik"]


@app.get("/",response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request" : request, "name" : name, "skills" : skills})
@app.get("/kontakt", response_class=HTMLResponse)
async def get_form(request: Request):
        return templates.TemplateResponse("kontakt.html", {"request" : request})
@app.post("/kontakt", response_class=HTMLResponse)
async def post_form(request: Request):
        return templates.TemplateResponse("kontakt.html", {"request" : request})

if __name__ == "__main__":
       import uvicorn 
       uvicorn.run(app, host="127.0.0.1", port=8000)








# app.mount("/static", StaticFiles(directory="static"), name="static")


# templates = Jinja2Templates(directory="templates")


# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse("item.html", {"request": request, "id": id})

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
name = "Erdal Erdogan"

skills =["Hard- und Software","Betriebssysteme", "Netzwerke", "Open Source Software", "Cloud Computing", "AWS", "Git", "Python, VSCode, css, html, js, php", "CMS", "Musik"]


@app.get("/",response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request" : request, "name" : name, "skills" : skills})

@app.get("/kontakt", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("contact.html", {"request" : request})

@app.post("/submit/")
async def submit_form(request: Request, name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    return templates.TemplateResponse("confirmation.html", {"request": request, "name": name})

if __name__ == "__main__":
       import uvicorn 
       uvicorn.run(app, host="127.0.0.1", port=8000)

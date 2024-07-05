from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory='html_directory')
url = 'https://freetestapi.com/api/v1/weathers'  
response = requests.get(url)
weather_data = response.json()


@app.get('/', response_class=HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse('index.html', context={'request': request})

@app.get("/all/", response_class=HTMLResponse)
def get_cities(request: Request):
    return templates.TemplateResponse("cities.html", context={"request": request, "cities": weather_data})

@app.get("/weather/{city}", response_class=HTMLResponse)
def get_weather_request(city: str, request: Request):
    weather = next((weather for weather in weather_data if weather["city"].lower() == city.lower()), None)
    if weather:
        return templates.TemplateResponse("home4.html", context={"request": request, "weather": weather})
    else:
        return templates.TemplateResponse("not_found.html", context={"request": request})
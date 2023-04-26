
from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
import requests


load_dotenv()

proxy_bp = Blueprint("proxy_bp", __name__)

location_key = os.environ.get("LOCATION_KEY")
weather_key = os.environ.get("WEATHER_KEY")

#GET LOCATION
@proxy_bp.route("/location",methods=["GET"])
def get_lat_lon():
    loc_query = request.args.get("query")
    if not loc_query:
        return {"message": "must provide query parameter (location)"}

    response = requests.get(
        "https://us1.locationiq.com/v1/search.php",
        params={"query": loc_query, "key":location_key, "format":"json"}
    )

    return jsonify(response.json())

#GET WEATHER
@proxy_bp.route("/weather",methods=["GET"])
def get_weather():
    lat_query = request.args.get("lat")
    lon_query = request.args.get("lon")
    if not lat_query or lon_query:
        return {"message": "must provide lat and lon parameters"}

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"lat": lat_query, "lon":lon_query, "appid":weather_key}
    )

    return response.json()
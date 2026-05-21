import requests
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")

def get_restaurants(city: str):
    """Отримує список ресторанів у вказаному місті за допомогою Google Places API."""

    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+{city}&key={GOOGLE_PLACES_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        restaurants = []
        for result in data.get("results", []):
            restaurant = {
                "name": result.get("name"),
                "address": result.get("formatted_address"),
                "rating": result.get("rating"),
                "user_ratings_total": result.get("user_ratings_total")
            }
            restaurants.append(restaurant)
        return restaurants
    else:
        return {"Error": "Error fetching restaurants for {city}"}
    
    

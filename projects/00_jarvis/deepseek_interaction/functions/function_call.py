import requests
from my_token import AMAP_API_KEY
from common import send_messages

def get_weather(location):
    """
    Retrieve weather information for a given location using AMAP API.
    Returns:
        dict: Weather data for the location
    """
    try:
        response = requests.get("https://restapi.amap.com/v3/weather/weatherInfo?city={}&key={}&output=json".format(location, AMAP_API_KEY))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error getting weather: {e}")
        return None

def get_location_based_on_ip():
    """
    Retrieve the user's location based on their IP address.
    """
    try:
        response = requests.get("https://restapi.amap.com/v3/ip?output=json&key={}".format(AMAP_API_KEY))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error getting location: {e}")
        return None

import requests
from my_token import AMAP_API_KEY, GOOGLE_SEARCH_API, GOOGLE_CSE_ID
from common import send_messages

def get_weather(location):
    """
    Fetches weather information for a specified location using the AMAP API.

    Args:
        location (str): The name of the city or location for which weather data is requested.

    Returns:
        dict: A dictionary containing detailed weather information, such as temperature, weather conditions,
              and other relevant data. Returns None if the request fails or an error occurs.

    Raises:
        requests.exceptions.RequestException: If there is an issue with the HTTP request to the AMAP API.
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
    Retrieves the user's approximate location based on their IP address using the AMAP API.

    Returns:
        dict: A dictionary containing location details such as city, province, and coordinates.
              Returns None if the request fails or an error occurs.

    Raises:
        requests.exceptions.RequestException: If there is an issue with the HTTP request to the AMAP API.
    """
    try:
        response = requests.get("https://restapi.amap.com/v3/ip?output=json&key={}".format(AMAP_API_KEY))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error getting location: {e}")
        return None

def get_search_results(keyword):
    """
    Retrieves search results for a given keyword using the Google Custom Search API.

    Args:
        keyword (str): The search term or phrase to query.

    Returns:
        dict: A dictionary containing search results, including titles, URLs, and snippets.
              Returns None if the request fails or an error occurs.

    Raises:
        requests.exceptions.RequestException: If there is an issue with the HTTP request to the Google API.
    """
    try:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "q" : keyword,
            "key" : GOOGLE_SEARCH_API,
            "cx" : GOOGLE_CSE_ID
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error getting search results: {e}")
        return None
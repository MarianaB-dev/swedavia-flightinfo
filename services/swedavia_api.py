import os
import requests

from datetime import date
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

# Swedavia FlightInfo API endpoint
API_URL = "https://api.swedavia.se/flightinfo/v2/query"


def get_flights(airport="ARN", flight_type="A", flight_date=None):
    """
    Get flight information from Swedavia API.

    flight_type:
        A = Arrivals
        D = Departures
    """

    api_key = os.getenv("SWEDAVIA_API_KEY")

    if not api_key:
        raise ValueError("Swedavia API key is missing.")

    if flight_date is None:
        flight_date = date.today().strftime("%y%m%d")

    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Accept": "application/json"
    }

    filter_query = (
        f"airport eq '{airport}' and "
        f"scheduled eq '{flight_date}' and "
        f"flightType eq '{flight_type}'"
    )

    params = {
        "filter": filter_query,
        "count": 25
    }

    response = requests.get(
        API_URL,
        headers=headers,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    return response.json()
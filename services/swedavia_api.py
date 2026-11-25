import os
import requests

from datetime import date, datetime
from dotenv import load_dotenv


load_dotenv()

API_URL = "https://api.swedavia.se/flightinfo/v2"


def get_flights(airport="ARN", flight_type="A", flight_date=None, flight_id=None):
    """
    Get arrival or departure information from Swedavia API.

    A = Arrivals
    D = Departures
    """

    api_key = os.getenv("SWEDAVIA_API_KEY")

    if not api_key:
        raise ValueError("Swedavia API key is missing.")

    if flight_type not in ["A", "D"]:
        raise ValueError("Flight type must be A or D.")

    if flight_date is None:
        flight_date = date.today().strftime("%Y-%m-%d")
    elif len(flight_date) == 6:
        flight_date = datetime.strptime(
            flight_date, "%y%m%d"
        ).strftime("%Y-%m-%d")

    endpoint = "arrivals" if flight_type == "A" else "departures"

    url = f"{API_URL}/{airport}/{endpoint}/{flight_date}"

    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Accept": "application/json"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    flights = data.get("flights", [])

    # Keep the same data structure used by app.py
    flight_key = "arrival" if flight_type == "A" else "departure"

    normalized_flights = [
        {flight_key: flight}
        for flight in flights
    ]

    # Filter by flight number, if provided
    if flight_id:
        normalized_flights = [
            flight for flight in normalized_flights
            if flight[flight_key].get("flightId", "").upper()
            == flight_id.upper()
        ]

    return {
        "flights": normalized_flights,
        "continuationtoken": data.get("continuationtoken")
    }

def check_heartbeat():
    """
    Check the availability of the Swedavia FlightInfo API.
    """

    api_key = os.getenv("SWEDAVIA_API_KEY")

    if not api_key:
        raise ValueError("Swedavia API key is missing.")

    url = f"{API_URL}/heartBeat"

    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Accept": "application/json"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    return {
        "available": response.ok,
        "status_code": response.status_code
    }

def query_flights(filter_expression, count=100, continuation_token=None):
    """
    Search flights using an OData filter expression.

    Supported filter fields include:
    Airport, FlightType, Scheduled and FlightId.
    """

    api_key = os.getenv("SWEDAVIA_API_KEY")

    if not api_key:
        raise ValueError("Swedavia API key is missing.")

    if not filter_expression or not filter_expression.strip():
        raise ValueError("OData filter expression cannot be empty.")

    if not 1 <= count <= 1000:
        raise ValueError("Count must be between 1 and 1000.")

    url = f"{API_URL}/query"

    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Accept": "application/json"
    }

    params = {
        "filter": filter_expression,
        "count": count
    }

    if continuation_token:
        params["continuationtoken"] = continuation_token

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    return response.json()

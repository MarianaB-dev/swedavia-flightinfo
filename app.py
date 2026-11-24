from flask import Flask, render_template, request
from datetime import datetime
from zoneinfo import ZoneInfo

from services.swedavia_api import get_flights


app = Flask(__name__)

PER_PAGE = 20


@app.route("/")
def home():

    flight_type = request.args.get("type", "A")
    search_query = request.args.get("flight", "").strip().upper()
    
    page = request.args.get("page", 1, type=int)
    page = max(page, 1)

    if flight_type not in ["A", "D"]:
        flight_type = "A"

    try:
        # Get flights from Stockholm Arlanda
        data = get_flights(
            airport="ARN",
            flight_type=flight_type,
            flight_id=search_query if search_query else None
        )

        flights = data.get("flights", [])

        # Convert flight times from UTC to Stockholm time
        stockholm_timezone = ZoneInfo("Europe/Stockholm")

        for flight in flights:
            details = flight.get(
                "arrival" if flight_type == "A" else "departure",
                {}
            )

            time_key = "arrivalTime" if flight_type == "A" else "departureTime"
            flight_time = details.get(time_key, {})

            scheduled_utc = flight_time.get("scheduledUtc")

            if scheduled_utc:
                try:
                    utc_time = datetime.fromisoformat(
                        scheduled_utc.replace("Z", "+00:00")
                    )

                    stockholm_time = utc_time.astimezone(
                        stockholm_timezone
                    )

                    flight_time["scheduledLocal"] = (
                        stockholm_time.strftime("%H:%M")
                    )

                except ValueError:
                    flight_time["scheduledLocal"] = "N/A"
            else:
                flight_time["scheduledLocal"] = "N/A"

        # Sort flights by scheduled UTC time
        def get_scheduled_time(flight):
            details = flight.get(
                "arrival" if flight_type == "A" else "departure",
                {}
            )

            time_key = (
                "arrivalTime" if flight_type == "A"
                else "departureTime"
            )

            flight_time = details.get(time_key, {})
            return flight_time.get("scheduledUtc") or "9999"

        flights.sort(key=get_scheduled_time)
        
        total_flights = len(flights)
        total_pages = (total_flights + PER_PAGE - 1) // PER_PAGE

        page = min(page, max(total_pages, 1))

        start = (page - 1) * PER_PAGE
        end = start + PER_PAGE

        flights = flights[start:end]
        
        error = None

    except Exception as e:
        flights = []
        error = str(e)

    return render_template(
        "index.html",
        flights=flights,
        flight_type=flight_type,
        search_query=search_query,
        error=error,
        page=page,
        total_pages=total_pages,
        total_flights=total_flights
    )


if __name__ == "__main__":
    app.run(debug=True)
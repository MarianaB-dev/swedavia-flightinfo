from services.swedavia_api import get_flights

def test_flight_api():
    try:
        print("Connecting to Swedavia FlightInfo API...")

        data = get_flights(
            airport="ARN",
            flight_type="A"
        )

        print("API connection successful!")

        if isinstance(data, dict):
            print("Response fields:", list(data.keys()))

            flights = data.get("flights", [])
                
            if flights:
                print("\nFirst flight:")
                print(flights[0])

            if isinstance(flights, list):
                print("Number of flights:", len(flights))
            else:
                print("Response received. Check its structure.")

        elif isinstance(data, list):
            print("Number of flights:", len(data))

        else:
            print("Response received:", type(data).__name__)

    except Exception as error:
        print("API connection failed:", error)


if __name__ == "__main__":
    test_flight_api()

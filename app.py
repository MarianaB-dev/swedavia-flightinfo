from flask import Flask, render_template

from services.swedavia_api import get_flights


app = Flask(__name__)


@app.route("/")
def home():

    try:
        # Get arrival flights from Stockholm Arlanda
        data = get_flights(
            airport="ARN",
            flight_type="A"
        )

        flights = data.get("flights", [])

        error = None

    except Exception as e:
        flights = []
        error = str(e)

    return render_template(
        "index.html",
        flights=flights,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)

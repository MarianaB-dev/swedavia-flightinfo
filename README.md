# Swedavia FlightInfo

A Python Flask web application for displaying flight information at Stockholm Arlanda Airport (ARN), using the Swedavia FlightInfo API v2.

## Project Overview

Swedavia FlightInfo is an educational web development project inspired by an original Python command-line application demonstrated in a course assignment.

The purpose of this project was to recreate and extend its main functionality in a web-based environment with a user-friendly interface.

The application retrieves flight information from the Swedavia API and presents it through separate pages for arrivals, departures, destination information and advanced flight searches.

## Features

### 1. Arrivals and Departures
- Display arriving and departing flights at Stockholm Arlanda Airport.
- Show scheduled flight times, flight numbers, airlines, origins, destinations and statuses.
- Display flight times in the Europe/Stockholm time zone.

### 2. Flight Search
- Search for flights by flight number.
- Display matching flight information.

### 3. Pagination
- Display 20 flights per page.
- Navigate between pages while preserving search parameters.

### 4. Destination Overview
- Browse destination information.
- Search destinations by country.
- Use a JSON dataset containing 94 city entries.

### 5. Advanced Flight Search
- Search departures from Arlanda.
- Search arrivals to Arlanda.
- Search by flight number.
- Search departures from other Swedish airports.
- Search arrivals at other Swedish airports.
- Use OData filters to retrieve matching results.

### 6. Automatic Demo
- Display upcoming arrivals and departures.
- Show flights scheduled within the next three hours.
- Refresh flight information every 60 seconds.
- Start and stop the demonstration.

### 7. API Heartbeat
- Check the availability of the Swedavia API connection.

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- REST API
- JSON
- OData
- Git and GitHub

## API Integration

This project uses the **Swedavia FlightInfo API v2** to retrieve flight information.

API credentials are stored in an environment variable and are not included in the repository.

## Project Structure

```text
swedavia-flightinfo/
│
├── services/
│   └── swedavia_api.py
│
├── static/
│   ├── css/
│      └── style.css
│   
│
├── templates/
│   ├── index.html
│   ├── destinations.html
│   ├── odata.html
│   └── demo.html
│
├── data/
│   └── city_country.json
│
├── app.py
├── test_api.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### Requirements

- Python 3
- pip
- A Swedavia FlightInfo API key

### 1. Clone the repository

```bash
git clone https://github.com/MarianaB-dev/swedavia-flightinfo.git
cd swedavia-flightinfo
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

On Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the API key

Create a `.env` file in the project root directory:

```text
SWEDAVIA_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own API key.

Do not commit your `.env` file to GitHub.

### 6. Run the application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## Learning Outcomes

Through this project, I gained practical experience in:

- Developing web applications with Python and Flask.
- Integrating external REST APIs.
- Processing JSON responses.
- Working with OData queries.
- Implementing search and pagination.
- Handling time zones and date-based data.
- Building interactive interfaces with JavaScript.
- Organizing application code into separate modules.
- Using Git and GitHub for version control.

## Project Status

Completed as an educational project.

## Author

**Mariana Baryliuk**

GitHub: [MarianaB-dev](https://github.com/MarianaB-dev)


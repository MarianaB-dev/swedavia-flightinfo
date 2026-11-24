# Phase 1: Research

## 1. Project Overview

The goal of this project is to recreate the Swedavia FlightInfo
application based on the provided reference video.

The project is part of the APL programme at Komvux in Stockholm.

The application will use flight information from the official
Swedavia FlightInfo API v2.

This is an independent educational recreation and is not an
official Swedavia application.

## 2. Information Gathering

The research was based on the following resources:

- Swedavia Developer Portal
- Official FlightInfo API v2 documentation
- The provided Buster Swedavia FlightInfo reference video
- APL project instructions

Official website:
https://apideveloper.swedavia.se/

API documentation:
https://apideveloper.swedavia.se/documentation

## 3. API Research

Swedavia FlightInfo API v2 is a REST API that provides
information about arriving and departing flights at
Swedavia airports.

The API provides the following query endpoint:

GET https://api.swedavia.se/flightinfo/v2/query

The query endpoint supports filtering flight information
using parameters such as Airport, FlightType, Scheduled
and FlightId.

The API uses IATA airport codes to identify airports.

Date and time values in API responses are provided in UTC.

API requests require authentication using a subscription
key in the HTTP header:

Ocp-Apim-Subscription-Key

The API provides information such as flight numbers,
airlines, airports, scheduled times, estimated times,
actual times and flight status.

## 4. Available Airports

The official documentation lists ten Swedavia airports:

- Stockholm Arlanda (ARN)
- Bromma Stockholm (BMA)
- Göteborg Landvetter (GOT)
- Malmö (MMX)
- Luleå (LLA)
- Umeå (UME)
- Åre Östersund (OSD)
- Visby (VBY)
- Ronneby (RNB)
- Kiruna (KRN)

## 5. Tools and Technologies

The planned development environment includes:

- Ubuntu 26.04 (WSL)
- Visual Studio Code
- Python
- Flask
- HTML
- CSS
- JavaScript
- Git
- GitHub

The final technology choices will be confirmed during
implementation.

## 6. Initial Development Plan

The planned development steps are:

1. Prepare the development environment.
2. Create the project structure.
3. Develop the web interface.
4. Connect the application to the Swedavia API.
5. Display arrival and departure information.
6. Implement search and filtering.
7. Test the application and fix errors.
8. Publish the source code on GitHub.

## 7. Research Challenges and Solutions

Challenge: Understanding the available API endpoints.

Solution: Review the official Swedavia API documentation
and identify the relevant endpoints.

Challenge: Understanding the expected application
functionality.

Solution: Analyse the provided reference video and
identify the main features.

Challenge: Organising the development process.

Solution: Divide the project into research, implementation,
testing and documentation phases.

## 8. Research Conclusion

The research identified the Swedavia FlightInfo API v2
as the intended data source for the project.

Python and Flask are the proposed technologies for
developing the web application.

The next phase is implementation, including the
development of the user interface and API integration.

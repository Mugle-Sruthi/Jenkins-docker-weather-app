Automated CI/CD Pipeline for a Dockerized Weather Forecast App Using Jenkins
This project demonstrates an Automated CI/CD pipeline for a Dockerized Weather Forecast App using Jenkins. It integrates Docker, Jenkins, and a Flask-based weather application that fetches data from the OpenWeatherMap API, providing users with real-time weather forecasts. The project automates the build, push, and deployment process using a Jenkins pipeline.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Table of Contents
Overview

Features

Technologies Used

Project Structure

Prerequisites

Setup Instructions

Dockerization Details

CI/CD Pipeline Details

Usage

Contributing

License
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Overview

The Weather Forecast App is a simple Flask-based web application that allows users to search for weather details for any city. The app is containerized using Docker, ensuring consistency across various environments. This project features an Automated CI/CD pipeline using Jenkins to automate the process of building, pushing, and deploying the application.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Features
Weather Forecast: Allows users to view weather information for any city, including temperature, humidity, wind speed, pressure, etc.

Real-Time Data: Fetches weather data from the OpenWeatherMap API.

User-Friendly Interface: A simple, clean, and easy-to-navigate UI.

CI/CD Pipeline: Automates the process of building, testing, and deploying the application using Jenkins.

Dockerized App: Containerized using Docker for portability and consistency across environments.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Technologies Used
Backend: Python, Flask

API: OpenWeatherMap API for fetching weather data

Frontend: HTML, CSS

Containerization: Docker

CI/CD: Jenkins

Version Control: GitHub

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Project Structure
.
├── Dockerfile                 # Docker setup for the app
├── app.py                     # Flask application logic
├── requirements.txt           # Python dependencies
├── jenkins-pipeline.groovy    # Jenkins pipeline script
├── static/                    # Static files (CSS, JavaScript)
│   └── style.css              # Custom CSS for the app UI
├── templates/                 # HTML templates for the Flask app
│   ├── create_user.html       # User registration page
│   ├── dashboard.html         # Dashboard showing weather info
│   └── index.html             # Login page
├── .env                       # Environment variables (API keys)
└── .gitignore                 # Git ignore file
.
------------------------------------------------------------------------___----------------------------------------------------------------------------------------------------------------------
Prerequisites
Before setting up the project, make sure you have the following tools installed:

Docker: To containerize the application.

Jenkins: To set up the automated pipeline.

Git: For version control and collaboration.

OpenWeatherMap API Key: You’ll need an API key to fetch weather data. Sign up here and save it in the .env file.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Setup Instructions
Clone the Repository
Clone the repository to your local machine:
git clone https://github.com/your-username/jenkins-docker-weather-app
cd jenkins-docker-weather-app
Build and Run the Docker Container
Build the Docker image and run the container:
docker build -t weather-app .
docker run -p 5000:5000 weather-app
Set up Jenkins
Set up a Jenkins server (instructions here).

Create a new pipeline project and configure it to use your repository.

Add the Jenkins pipeline script (jenkins-pipeline.groovy) to the pipeline configuration.

Configure Environment Variables
Create a .env file in the root directory with your OpenWeatherMap API key:
WEATHER_API_KEY=your_api_key_here

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Dockerization Details
The Dockerfile defines the steps to containerize the application. Below is the content of the Dockerfile used:

dockerfile
-Use Python 3.12 as the base image
FROM python:3.12-slim

- Set the working directory inside the container
WORKDIR /app

- Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

- Copy the rest of the application code
COPY . .

- Expose port 5000 for the Flask app
EXPOSE 5000

- Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

- Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CI/CD Pipeline Details
The Jenkins pipeline automates the entire process of building, pushing, and deploying the Dockerized app. The pipeline is defined in the jenkins-pipeline.groovy file, and the stages are as follows:

Checkout: Pulls the latest code from GitHub.

Build & Push Docker Image: Builds the Docker image and pushes it to Docker Hub.

Deploy: Deploys the new Docker image by stopping any previous instances and running the new one.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Usage

To run the application in development mode:

docker build -t weather-app .

docker run -p 5000:5000 weather-app

-Access the application in your browser: http://localhost:5000

To stop the container:

docker ps  # Find the container ID

docker stop <container_id>

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.

Create a new branch for your feature or fix.

Make your changes and test them.

Submit a pull request.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
License
This project is licensed under the MIT License. See the LICENSE file for more details.



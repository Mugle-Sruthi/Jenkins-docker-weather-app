Automated CI/CD Pipeline for a Dockerized Weather Forecast App Using Jenkins
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This project demonstrates an Automated CI/CD pipeline for a Dockerized Weather Forecast App using Jenkins. It integrates Docker, Jenkins, and a Flask-based weather application that fetches data from the OpenWeatherMap API, providing users with real-time weather forecasts. This project automates the build, push, and deployment of the application using a Jenkins pipeline.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Table of Contents
Overview

1.Features

2.Technologies Used

3.Project Structure

4.Prerequisites

5.Setup Instructions

6.Dockerization Details

7.CI/CD Pipeline Details

8.Usage

9.Contributing

10.License

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Overview
The Weather Forecast App is a simple Flask-based web application that allows users to search for weather details of any city. The app is containerized using Docker, ensuring consistency across different environments. It features an Automated CI/CD pipeline set up using Jenkins to automate the build, push, and deployment process, ensuring seamless and rapid deployment of new changes.

1.Features
Weather Forecast: View weather information for any city, including temperature, humidity, wind speed, pressure, and more.

Real-time Data: Fetches real-time weather data from the OpenWeatherMap API.

User-Friendly Interface: Simple, clean, and easy-to-navigate UI.

CI/CD Pipeline: Automates the process of building, testing, and deploying the application using Jenkins.

Dockerized App: The application is containerized with Docker to ensure portability and consistency.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2.Technologies Used
Backend: Python, Flask

API: OpenWeatherMap API for weather data

Frontend: HTML, CSS

Database: None (Static data from API)

Containerization: Docker

CI/CD: Jenkins

Version Control: GitHub

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
3.Project Structure

.
├── Dockerfile                 # Docker setup for the app
├── app.py                     # Flask application logic
├── requirements.txt           # Python dependencies
├── jenkins-pipeline.groovy    # Jenkins pipeline script
└── static/                    # Static files (CSS, JavaScript)
└── templates/                 # HTML templates
└── .env                       # Environment variables
└── .gitignore                 # Git ignore file

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
4.Prerequisites
Ensure you have the following installed:

Docker

Jenkins

Git

OpenWeatherMap API key (stored in .env file)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
5.Setup Instructions
Clone the Repository
Clone the repository to your local machine:


git clone https://github.com/your-username/jenkins-docker-weather-app
cd jenkins-docker-weather-app
Build and Run the Docker Container
Build the Docker image and run the container:


docker build -t weather-app .
docker run -p 5000:5000 weather-app
Set up Jenkins
Set up a Jenkins server.

Create a new pipeline project and configure it to use your repository.

Add the Jenkins pipeline script (jenkins-pipeline.groovy) to the Jenkins pipeline configuration.

Configure Environment Variables
Create a .env file in the root directory with your OpenWeatherMap API key:


WEATHER_API_KEY=your_api_key_here
Jenkins Pipeline
The Jenkins pipeline automates the process of building the Docker image, pushing it to Docker Hub, and deploying the application to a server. The pipeline includes the following stages:

Checkout: Pulls the latest code from GitHub.

Build & Push Docker Image: Builds the Docker image and pushes it to Docker Hub.

Deploy: Stops any previous instances of the app and runs the new Docker container.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Dockerization Details
The Dockerfile defines the steps to containerize the application. Here's the Dockerfile used:
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
6.dockerfile

--> Use Python 3.12 as the base image
FROM python:3.12-slim

 -->Set the working directory inside the container
WORKDIR /app

--> Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

-->Copy the rest of the application code
COPY . .

--> Expose port 5000 for the Flask app
EXPOSE 5000

--> Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

--> Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
7.CI/CD Pipeline Details
The Jenkins pipeline automates the entire process, including building, pushing, and deploying the Dockerized app. The pipeline is defined in the jenkins-pipeline.groovy file, which includes the following stages:

Checkout: Pulls the latest code from GitHub.

Build & Push Docker Image: Builds the Docker image and pushes it to Docker Hub.

Deploy: Deploys the new image by stopping the current container and running the new one.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
8.Usage
To run the application in development mode:


docker build -t weather-app .
docker run -p 5000:5000 weather-app
Access the application in your browser:

Website: http://localhost:5000

To stop the container:

docker ps  Find the container ID
docker stop <container_id>

---->>FOR MORE DETAILS 
KINDLY REFER REPORT FILE 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
9.Contributing
Contributions are welcome! Please fork the repository, create a new branch for your feature or fix, and submit a pull request.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
10.License
This project is licensed under the MIT License. See the LICENSE file for more details.

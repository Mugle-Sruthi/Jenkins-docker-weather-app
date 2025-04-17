#Dockerfile 

#Use official python image
FROM python:3.12-slim

#set working directory
WORKDIR /app

#Cpy requirements first to leverage  Docker cache 
COPY requirements.txt .

#Install python dependencies 
RUN pip install --no-cache-dir -r requirements.txt

#copy the rest of the application
COPY . .

#Expose the port the app runs on 
EXPOSE 5000

#set environment variables 
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

#Run the application
CMD ["flask", "run", "--host=0.0.0.0"]


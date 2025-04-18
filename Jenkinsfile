pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'sruthimugle19/weather-app'  // Updated with your Docker Hub username
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Mugle-Sruthi/jenkins-docker-weather-app.git'
            }
        }
        stage('Build & Push Docker Image') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE}:latest")
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-creds') {  // Use your credential ID here
                        docker.image("${env.DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop weather-app || true'
                sh 'docker rm weather-app || true'
                sh "docker run -d -p 5000:5000 --env-file .env --name weather-app ${env.DOCKER_IMAGE}:latest"  // Added --env-file
            }
        }
    }
}

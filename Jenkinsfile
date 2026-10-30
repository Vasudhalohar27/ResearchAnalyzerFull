pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout GitHub') {
            steps {
                checkout scm
            }
        }

        stage('Check Docker') {
            steps {
                bat 'docker --version'
                bat 'docker compose version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t research-analyzer:jenkins .'
            }
        }
    }

    post {
        success {
            echo 'Research Analyzer Docker build completed successfully!'
        }
        failure {
            echo 'Build failed. Check Console Output.'
        }
    }
}
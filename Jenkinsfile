pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from the version control system (e.g., GitHub)
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                
                // Install project dependencies (if not using a virtual environment)
                sh 'pip install -r requirements.txt'

                // Run your tests using pytest
                sh 'python3 -m pytest tests/test_app.py'
            }
        }

        // Add more stages for deployment, if needed
        // ...
    }

    post {
        always {
            // Archive test reports (if applicable)
            junit 'test-reports/**/*.xml'
        }
    }
}

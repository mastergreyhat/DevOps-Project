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
                // Define the Python environment (use a virtual environment or global Python installation)
                script {
                    // Example: Use a virtual environment
                    def venv = tool name: 'Python 3.9', type: 'hudson.plugins.python.PythonInstallation'
                    sh "${venv}/bin/python -m venv myvenv"
                    sh "source myvenv/bin/activate"
                }
                
                // Install project dependencies (if not using a virtual environment)
                sh 'pip install -r requirements.txt'

                // Run your tests using pytest
                sh 'python -m pytest tests/test_app.py'
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

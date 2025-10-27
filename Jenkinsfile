pipeline {
    agent any
    stages {
        stage('Run Selenium Tests with pytest') {
            steps {
                    echo "Running Selenium Tests using pytest"
                    bat 'pip install -r requirements.txt'
                    bat 'start /B python app.py'
                    bat 'ping 127.0.0.1 -n 5 > nul'
                    bat 'pytest -v'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t seleniumdemoapp:v1 ."
            }
        }
        stage('Docker Login') {
            steps {
                  bat 'docker login -u sowmya959 -p Sowmyairuku@12'
                }
            }
        stage('push Docker Image to Docker Hub') {
            steps {
                echo "push Docker Image to Docker Hub"
                bat "docker tag seleniumdemoapp:v1 sowmya959/sample:seleniumtestimage"               
                    
                bat "docker push sowmya959/sample:seleniumtestimage"
                
            }
        }
        stage('Deploy to Kubernetes') { 
            steps { 
                    bat 'kubectl apply -f deployment.yaml --validate=false' 
                    bat 'kubectl apply -f service.yaml' 
            } 
        }
    }
    post {
        success {
            echo 'successfull!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
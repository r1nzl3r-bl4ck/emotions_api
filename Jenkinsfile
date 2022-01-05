pipeline {
    agent {
        docker {
            image 'python:3'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt --user'
            }
        }
        stage('Docker Build & Push') {
            steps {
                script {
                  docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
                    def apppythonjenkins = docker.build("r1nzler/emotions-api:${gitcommit}", ".")
                    apppythonjenkins.push()
                  }
                }
            }
        }
    }
}

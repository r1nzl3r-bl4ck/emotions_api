pipeline {
    agent {
        docker {
            image 'python:3'
        }
    }
    stages {
        stage('Build') {
            steps {

                sh 'python -m pip install --user -r requirements.txt'
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

pipeline {
    agent any
    environment {
        gitcommit = "${gitcommit}"
    }
    stages {
        stage('Build') {
            agent {
              docker {
                image 'python:3'
              }
            }
            environment {
              HOME = "${env.WORKSPACE}"
            }
            steps {
                sh 'pip install -r requirements.txt --user'
            }
        }
        stage('Docker Build & Push') {
            steps {
                sh 'echo ${gitcommit}'
                script {
                  docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
                    def apppythonjenkins = docker.build("r1nzler/emotions-api:latest", ".")
                    apppythonjenkins.push()
                  }
                }
            }
        }
    }
}


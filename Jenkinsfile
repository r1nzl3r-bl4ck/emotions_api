pipeline {
    agent {
        docker {
            image 'python:3.7.2'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'sudo pip3 install --upgrade pip3 && sudo pip3 install -r requirements.txt --user'
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






pipeline {
    agent any
    stages {
        stage('Verify Branch') {
            steps {
                echo "$GIT_BRANCH"
            }
        }
        stage('Docker Build') {
            steps {
                sh(script: 'docker images -a')
                sh(script: '''
                docker images -a
                docker build -t emotions-api .
                docker images -a
                ''')
            }
        }
        stage('Push Container') {
            steps{
                echo "Workspace is $WORKSPACE"
                dir("$WORKSPACE") {
                    script {
                        docker.withRegistry('https://index.docker.io/v1/', 'DockerHub') {
                            def image = docker.build('r1nzler/emotions-api:latest')
                            image.push()
                        }
                    }
                }
            }
        }
        stage('Container Scanning') {
            stage('Run Trivy') {
               steps {
                  sh(script: '''
                  trivy image r1nzler/emotions-api
                  ''')
               }
            }
        }
    }
}


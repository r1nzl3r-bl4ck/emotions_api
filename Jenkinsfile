pipeline {
    agent any
    environment {
        tag = sh(returnStdout: true, script: "git rev-parse --short=10 HEAD")
    }
    stages {
        stage('Verify Branch') {
            steps {
                echo "$GIT_BRANCH"
            }
        }
        stage('Printing the TAG') {
            steps {
                echo "$tag"
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
                echo "Current TAG is ${env.GIT_COMMIT[0..6]}"
                dir("$WORKSPACE") {
                    script {
                        docker.withRegistry('https://index.docker.io/v1/', 'DockerHub') {
                            def image = docker.build("r1nzler/emotions-api:${env.GIT_COMMIT[0..7]}")
                            image.push()
                        }
                    }
                }
            }
        }
        stage('Run Trivy') {
            steps {
                echo "Here Trivy will run for vuln testing"
                // sh(script: '''
                // trivy image --exit-code 1 --severity CRITICAL r1nzler/emotions-api
                // ''')
            }
        }
    }
}



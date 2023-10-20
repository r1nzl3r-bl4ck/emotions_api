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
                environment {
                    GIT_COMMIT = sh(returnStdout: true, script: "git rev-parse --short=10 HEAD")
                }
                echo "Workspace is $GIT_COMMIT"
                echo "Current TAG is $tag"
                dir("$WORKSPACE") {
                    script {
                        docker.withRegistry('https://index.docker.io/v1/', 'DockerHub') {
                            def image = docker.build("r1nzler/emotions-api:GIT_COMMIT")
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



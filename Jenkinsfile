pipeline {
    agent any
    environment {
        tag_long = sh(returnStdout: true, script: "git rev-parse --short=10 HEAD")
        tag_short = sh(returnStdout: true, script: "git rev-parse --short=10 HEAD")
        tag_opt = sh(returnStdout: true, script: "git rev-parse --short=10 HEAD").trim()
    }
    stages {
        stage('Verify Branch') {
            steps {
                echo "$GIT_BRANCH"
            }
        }
        stage('Printing the TAG') {
            steps {
                echo "The long tag is $tag_long"
                echo "The short tag is $tag_short"
                echo "The opt tag is $tag_opt"
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



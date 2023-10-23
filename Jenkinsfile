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
                echo "Current TAG is ${env.GIT_COMMIT[0..7]}"
                dir("$WORKSPACE") {
                    script {
                        docker.withRegistry('https://index.docker.io/v1/', 'DockerHub') {
                            def image = docker.build("r1nzler/emotions-api:${GIT_COMMIT[0..7]}")
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
        stage('Update k8s Deployment') {
            steps {
                sh '''
                echo "Updating kubernetes deployment with the image ${env.GIT_COMMIT[0..7]}"
                '''
            }
        }
    }
}



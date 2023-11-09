pipeline {
    agent any
    stages {
        stage('Verify Branch') {
            steps {
                echo "$GIT_BRANCH"
            }
        }
        stage('SonarQube Analysis') {
            def scannerHome = tool 'SonarScanner';
            withSonarQubeEnv() {
              sh "${scannerHome}/bin/sonar-scanner"
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
        stage('Update k8s Deployment') {
            steps {
                withCredentials([string(credentialsId: 'Github Connection', variable: 'GH_PAT')]) {
                    sh '''
                    echo "Updating kubernetes deployment with the image ${GIT_COMMIT:0:8}"
                    rm -rf k8s-apps/
                    git clone https://${GH_PAT}@github.com/r1nzl3r-bl4ck/k8s-apps.git
                    cd k8s-apps/emotions-api/
                    sed -E -i'' "s/(.*r1nzler\\/emotions-api:).*/\\1${GIT_COMMIT:0:8}/" 'deployment.yaml'
                    cat deployment.yaml
                    echo "Pushing changes to github..."
                    git add .
                    git commit -m "[JENKINS BOT] Updating k8s deployment image tag."
                    git push origin main
                    '''
                }
            }
        }
    }
}



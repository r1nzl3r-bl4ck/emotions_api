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
                sh(script: '/usr/bin/docker images -a')
                sh(script: '''
                /usr/bin/docker images -a
                /usr/bin/docker build -t emotions-api .
                /usr/bin/docker images -a
                ''')
            }
        }
    }
}


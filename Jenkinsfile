pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '. .venv/bin/activate && pytest -v'
            }
        }

        stage('Package Source') {
            steps {
                sh 'tar --exclude=.git --exclude=.venv --exclude=__pycache__ -czf todo-api-source.tar.gz app.py test_app.py requirements.txt Dockerfile'
                archiveArtifacts artifacts: 'todo-api-source.tar.gz', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Todo API CI pipeline finished.'
        }
    }
}

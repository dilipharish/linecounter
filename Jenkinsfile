pipeline {
    agent any

    stages {
        stage('Run Python Line Counter') {
            steps {
                echo '🚀 Running line counter...'
                sh 'python line_counter.py'
            }
        }
    }
}

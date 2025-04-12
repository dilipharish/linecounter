pipeline {
    agent any

    stages {
        stage('Run Python Line Counter') {
            steps {
                echo '🚀 Running line counter...'
                bat 'python line_counter.py example.txt'
            }
        }
    }
}

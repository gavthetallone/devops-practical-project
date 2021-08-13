pipeline{
    agent any
    environment{
        DATABASE_URI = credentials("DATABASE_URI")
        MYSQL_ROOT_PASSWORD = credentials("MYSQL_ROOT_PASSWORD")
        MYSQL_DATABASE = credentials("MYSQL_DATABASE")
        DOCKER_CREDENTIALS = credentials("DOCKER_CREDENTIALS")
    }
    stages{
        stage('Install Dependencies'){
            steps{
                sh "bash scripts/setup.sh"
            }
        }
        stage('Run Unit Tests'){
            steps{
                sh "bash scripts/test.sh"
            }
            post {
                always {
                step([$class: 'CoberturaPublisher', coberturaReportFile: 'output/coverage/jest/cobertura-coverage.xml'])
                junit 'output/coverage/junit/junit.xml'
                }
            }
        }
        stage('Build and Push Images'){
            steps{
                sh "bash scripts/build.sh"
            }
        }
        stage('Configure Swarm'){
            steps{
                sh "bash scripts/config.sh"
            }
        }
        stage('Deploy Stack'){
            steps{
                sh "bash scripts/deploy.sh"
            }
        }
    }
}
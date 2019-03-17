pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		sh 'python *.py'
            }
        }
        stage('Code-Analysis') {
              steps {
                echo 'Analysing the code..'
                withSonarQubeEnv('sonarqube') {
                sh 'sonar-scanner'
              }	
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		sh 'python -m compileall *.py'
            }
        }
        stage('Code-Analysis') {
              steps {
                echo 'Analysing the code..'
                tools {
                   sonarQube 'sonar scanner'
                }
                withSonarQubeEnv('sonarqube') {
                sh 'sonar-scanner'
              }	
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'python *.pyc'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'mkdir Delivery'
                sh 'cp Firstpythonclass.pyc Delivery/'
            }
        }
    }
}

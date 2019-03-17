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
                python *.pyc
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                mkdir Delivery
                cp Firstpythonclass.pyc Delivery/
            }
        }
    }
}

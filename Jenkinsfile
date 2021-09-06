pipeline {
	agent any
	    stages {

		stage('Clone Repository') {

			/* Cloning the repository to our workspace */
			steps {
				checkout scm
				}
	   }
		
		stage('Build Image') {
	        steps {
	        sh 'sudo docker build -t nlp-python:v1 .'
	        }
	   }
	   stage('Stop container') {
	        steps {
	        sh 'sudo docker stop nlpmodel'
			sh 'sudo docker rm -f nlpmodel'
	        }
	   }
	   stage('Run Image') {
	        steps {
	        sh 'sudo docker run -d -p 5010:4000 nlpmodel nlp-python:v1'
	        }
	   }
		
	   stage('Testing'){
	        steps {
	            echo 'Testing..'
	            }
	   }
    }
}

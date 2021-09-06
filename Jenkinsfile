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
	        sh 'sudo docker build -t ask_budget:v1 .'
	        }
	   }
	   stage('Stop container') {
	        steps {
	        sh 'sudo docker stop budget'
			sh 'sudo docker rm -f budget'
	        }
	   }
	   stage('Run Image') {
	        steps {
	        sh 'sudo docker run -d -p 5011:4000 budget ask_budget:v1'
	        }
	   }
		
	   stage('Testing'){
	        steps {
	            echo 'Testing..'
	            }
	   }
    }
}

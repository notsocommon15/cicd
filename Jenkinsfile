#!/usr/bin/env groovy

pipeline {
 
 agent any
 
 environment {
		DOCKERHUB_CREDENTIALS=credentials('docker-hub')
	}

 stages {
 
	stage('Initialize'){
	   steps{
		script{
			def dockerHome = tool 'docker'
			env.PATH = "${dockerHome}/bin:${env.PATH}"
		}
	  }
	}
	  
    stage('build') {
	    agent { docker { image 'python:3.8.5-alpine' } }
      steps {
        sh 'pip install -r requirements.txt && python ${WORKSPACE}/src/test.py'
      }
    }

    
    //stage('test') {
	//agent { docker { image 'python:3.8.5-alpine3.12' } }
      //steps {
        //sh 'python ${WORKSPACE}/src/test.py'
      //}
    //}
	
    stage('Docker Image') {
      steps{
	      sh 'docker build -t personal-python-test:latest .'
		  }
        }

   // stage('Login') {

		//	steps {
		//		sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR -p --password-stdin'
		//	}
	//	}
	//	stage('Push') {

		//	steps {
			//	sh 'docker push kediasubham/personal-python-test:latest'
		//	}
	//	}



    stage('Run Image / Container Creation') {
        steps{
		sh 'docker run -p 5000:5000 -d --name myfirstcontainer:$BUILD_NUMBER personal-python-test:latest'
		}
    }
  }
}





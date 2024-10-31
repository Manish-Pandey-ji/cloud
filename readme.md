After all this coding 
Make sure you install all neccesary plugin in jenkin.
Give the public ip in ansible/inventories/hosts.

At last run the code in your local system
ansible-playbook -i ansible/inventories/hosts deploy.yml --become

it run your docker file in your remote machine

Below is the Jenkinsfil pipeline

''''
pipeline {
    agent any
    environment {
        GITHUB_TOKEN = credentials('github')
    }

    stages {
        stage('Clone') {
            steps {
                git url: 'https://github.com/Manish-Pandey-ji/cloud.git',
                branch: 'main',
                credentialsId: 'github'
            }
        }
        stage('Build Backend') {
            steps {
                dir('backend') {
                    sh 'mvn package'
                    sh 'docker build -t backend-service .'
                }
            }
        }
        stage('Build Frontend') {
            steps {
                dir('fronted') {
                    sh 'docker build -t frontend-service .'
                }
            }
        }
        stage('Push to Registry') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        sh 'docker tag backend-service manishpandey123/backend-service'
                        sh 'docker tag frontend-service manishpandey123/frontend-service'
                        sh 'docker push manishpandey123/backend-service'
                        sh 'docker push manishpandey123/frontend-service'
                    }
                }
            }
        }
    }
}
'''''

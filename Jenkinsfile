pipeline {
    agent any
        stages {
            stage('Checkout') {
                steps {
                    checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '66e40ed7-9eb2-4b88-8148-b4c9ef556595', url: 'https://github.com/great800/WorldOfGames.git']]])
                }
            }
            stage('Build') { 
                steps {
                    bat 'docker build -t jenkinsdocker:latest .'
                }
            }
            stage('Run') { 
                steps {
                    bat 'docker compose up -d'
                }
            }
            stage('Test') { 
                steps {
                     git branch: 'main', credentialsId: '66e40ed7-9eb2-4b88-8148-b4c9ef556595', url: 'https://github.com/great800/WorldOfGames.git'
                     bat 'python e2e.py'
                }
            }
            stage('Finalize') {
                steps {
                    bat 'docker compose stop'
                    bat 'docker tag jenkinsdocker great800/jenkinsdocker:latest'
	                bat 'docker push great800/jenkinsdocker:latest'
                }
            }
        }   
}
/*
JenkinsFile (WorldOfGames – Lior A)

Stages
1. Checkout - checkout the repository.
2. Build - Build our docker image.
3. Run - will run our dockerized application. The application will expose the port 8777 on
localhost, and a dummy Scores.txt will be mounted to it in order to server the results for
the tests.
4. Test - With our e2e.py file it will selenium test our scores web service and fail the
pipeline if the tests failed.
5. Finalize - Will terminate our tested container and push to DockerHub the new image we created
*/
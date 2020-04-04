pipeline {
  agent any
  stages {
    stage('Python Req.') {
      steps {
        sh 'pip3 install -r requirements.txt'
      }
    }

    stage('Python Lint') {
      steps {
        sh 'pylint --disable=W0311 html_generator.py'
      }
    }

    stage('Generate HTML') {
      steps {
        sh 'python3 html_generator.py'
      }
    }

    stage('Build & Push') {
      steps {
        sh '''aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 628641662978.dkr.ecr.eu-west-1.amazonaws.com/capstone
docker -H=tcp://localhost:2375 build -t capstone .
docker -H=tcp://localhost:2375 tag capstone:latest 628641662978.dkr.ecr.eu-west-1.amazonaws.com/capstone:latest
docker -H=tcp://localhost:2375 push 628641662978.dkr.ecr.eu-west-1.amazonaws.com/capstone:latest
'''
      }
    }

    stage('Docker Container') {
      steps {
        sh 'docker -H=tcp://localhost:2375 container run -d 628641662978.dkr.ecr.eu-west-1.amazonaws.com/capstone:latest'
      }
    }

    stage('Deployment') {
      steps {
        sh '''kubectl apply -f kubernetes/deployment.yml
kubectl apply -f kubernetes/loadbalancer.yml'''
      }
    }

    stage('Rollout Deployment') {
      steps {
        sh 'kubectl rollout restart deployment/webserver'
      }
    }

  }
}
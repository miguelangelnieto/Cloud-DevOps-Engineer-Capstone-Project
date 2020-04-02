pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
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

    stage('Docker WebServer') {
      steps {
        sh 'docker-compose -H tcp://localhost:2375 -t miguelangel/webserver'
      }
    }

  }
}
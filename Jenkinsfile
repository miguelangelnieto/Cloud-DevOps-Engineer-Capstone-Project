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

  }
}
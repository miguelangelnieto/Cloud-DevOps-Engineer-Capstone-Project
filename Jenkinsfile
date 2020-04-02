pipeline {
  agent any
  stages {
    stage('Python Req.') {
      steps {
        sh 'pip3 install -r requirements.txt'
      }
    }

    stage('Pylint') {
      steps {
        sh 'pylint html_generator.py'
      }
    }

  }
}
pipeline {
  agent any
  stages {
    stage('Python') {
      steps {
        sh 'pip3 install -r requirements.txt'
        sh 'python --version'
      }
    }

  }
}
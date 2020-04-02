pipeline {
  agent any
  stages {
    stage('Python') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'python --version'
      }
    }

  }
}
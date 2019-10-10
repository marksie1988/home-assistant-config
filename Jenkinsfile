pipeline {
  agent none
  stages {
    stage('YAML') {
      agent {
        docker {
          image 'pipelinecomponents/yamllint:latest'
        }

      }
      steps {
        sh 'yamllint .'
      }
    }
    stage('Remark') {
      agent {
        docker {
          image 'pipelinecomponents/remark-lint'
        }

      }
      steps {
        sh 'remark --no-stdout --color --frail --use preset-lint-recommended .'
      }
    }
  }
}
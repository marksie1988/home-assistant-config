pipeline {
  agent none
  stages {
    stage('Remark') {
      agent {
        docker {
          args 'remark --no-stdout --color --frail --use preset-lint-recommended .'
          image 'zemanlx/remark-lint'
        }

      }
      steps {
        sh 'remark --no-stdout --color --frail --use preset-lint-recommended .'
      }
    }
    stage('YAML Check') {
      agent {
        docker {
          image 'pipelinecomponents/yamllint:latest'
        }

      }
      steps {
        sh 'yamllint .'
      }
    }
  }
}
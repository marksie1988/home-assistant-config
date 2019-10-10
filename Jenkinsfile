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
    stage('home_assistant_stable') {
      parallel {
        stage('home_assistant_stable') {
          agent {
            docker {
              image 'homeassistant/home-assistant:stable'
            }

          }
          steps {
            sh 'cp -R ./.stubs/* ./config'
            sh 'python -m homeassistant --version'
            sh 'python -m homeassistant --config ./config/ --script check_config --info all'
          }
        }
        stage('home_assistant_beta') {
          agent {
            docker {
              image 'homeassistant/home-assistant:beta'
            }

          }
          steps {
            sh 'cp -R ./.stubs/* ./config'
            sh 'python -m homeassistant --version'
            sh 'python -m homeassistant --config ./config/ --script check_config --info all'
          }
        }
        stage('home_assistant_dev') {
          agent {
            docker {
              image 'homeassistant/home-assistant:dev'
            }

          }
          steps {
            sh 'cp -R ./.stubs/* ./config'
            sh 'python -m homeassistant --version'
            sh 'python -m homeassistant --config ./config/ --script check_config --info all'
          }
        }
      }
    }
  }
}
pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 30, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '15'))
    }

    parameters {
        choice(
            name: 'TEST_SCOPE',
            choices: ['all', 'smoke', 'regression'],
            description: 'Which tests to run'
        )
    }

    environment {
        VENV_DIR = '.venv'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                bat """
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate
                    python -m pip install --upgrade pip
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    pip install -r requirements.txt
                    playwright install --with-deps
                """
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def markerArg = ''
                    if (params.TEST_SCOPE == 'smoke') {
                        markerArg = '-m smoke'
                    } else if (params.TEST_SCOPE == 'regression') {
                        markerArg = '-m regression'
                    }

                    bat """
                        call %VENV_DIR%\\Scripts\\activate
                        pytest ${markerArg} --junitxml=reports/junit.xml
                    """
                }
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/junit.xml'

            publishHTML(target: [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report'
            ])

            archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
        }

        failure {
            echo 'Build failed — check the Pytest HTML Report and console output for details.'
        }

        success {
            echo 'All tests passed.'
        }
    }
}

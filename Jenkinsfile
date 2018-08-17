pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'checkout'
                checkout scm
            }
        }
        stage('Retrieve from EDU') {
            steps {
                echo 'Retrieve from EDU'
                // TBD
            }
        }
        stage('process HWs') {
            parallel {
                stage('Execute Unit-tests') {
                    steps {
                        echo 'Execute Unit-tests'
                        // TBD
                    }
                }
                stage('Conventions Check') {
                    steps {
                        echo 'Conventions Check'
                        // TBD
                    }
                }
                stage('Metrics Report') {
                    steps {
                        echo 'Metrics Report'
                        // TBD
                    }
                }
                stage('Generate Word File') {
                    steps {
                        echo 'Generate Word File'
                        // TBD
                    }
                } 
            } // Parallel
        } // stage - process HWs
        stage('Generate Feedback Skeleton') {
            steps {
                echo 'Generate Feedback Skeleton'
                // TBD
            }
        }
    } // stages             
} // pipeline

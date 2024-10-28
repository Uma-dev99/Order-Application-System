// pipeline {
//     agent any
    
//     environment {
//         IMAGE_NAME = 'order_management'
//         IMAGE_TAG = 'latest'
//         CONTAINER_NAME = 'order_management_container'
//         GIT_URL = 'https://github.com/Uma-dev99/Order-Application-System.git' URL
//         GIT_BRANCH = 'main' 
//     }

//     stages {
//         stage('Checkout Code') {
//             steps {
//                 git url: "${GIT_URL}", branch: "${GIT_BRANCH}"
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 script {
//                     powershell "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
//                 }
//             }
//         }
//         stage('Run Application') {
//             steps {
//                 script {
//                     // powershell """
//                     //     if (docker ps -q -f name=${CONTAINER_NAME}) {
//                     //         docker stop ${CONTAINER_NAME}
//                     //         docker rm ${CONTAINER_NAME}
//                     //     }
//                     // """                    
//                     // Stop and remove any previous container with the same name
//                     bat "docker stop ${CONTAINER_NAME} || echo 'No running container to stop'"
//                     bat "docker rm ${CONTAINER_NAME} || echo 'No container to remove'"
                    
//                     // Run the Docker container
//                     bat "docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}:${IMAGE_TAG}"
//                     // powershell "docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}:${IMAGE_TAG}"
//                 }
//             }
//         }
//     }

//     post {
//         always {
//             echo "Cleaning up unused Docker images and containers to save space."
//             // powershell 'docker image prune -f'
//             // powershell 'docker container prune -f'
//             bat 'docker image prune -f'
//             bat 'docker container prune -f'
//         }
//         success {
//             echo 'The application was successfully deployed and is running.'
//         }
//         failure {
//             echo 'The deployment failed. Please check the logs for more details.'
//         }
//     }
// }

pipeline {
    agent any
    
    environment {
        IMAGE_NAME = 'order_management'
        IMAGE_TAG = 'latest'
        CONTAINER_NAME = 'order_management_container'
        GIT_URL = 'https://github.com/Uma-dev99/Order-Application-System.git' 
        GIT_BRANCH = 'main' 
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout code from the specified Git repository and branch
                git url: "${GIT_URL}", branch: "${GIT_BRANCH}"
            }
        }

        stage('Build Docker Image') {
            steps {
                node{
                    // Build the Docker image
                    bat "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Run Application') {
            steps {
                node{
                    // Stop and remove any previous container with the same name
                    bat "docker stop ${CONTAINER_NAME} || echo 'No running container to stop'"
                    bat "docker rm ${CONTAINER_NAME} || echo 'No container to remove'"

                    // Run the Docker container
                    bat "docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up unused Docker images and containers to save space."
            // Clean up unused Docker images and containers
            bat 'docker image prune -f'
            bat 'docker container prune -f'
        }
        success {
            echo 'The application was successfully deployed and is running.'
        }
        failure {
            echo 'The deployment failed. Please check the logs for more details.'
        }
    }
}

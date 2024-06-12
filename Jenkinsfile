pipeline {
    agent any

    stages {
        stage('Build Backend') {
            steps {
                dir('backend') {
                    script {
                        def backendImage = docker.build("vf_firsttask-backend")
                    }
                }
            }
        }

        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    script {
                        docker.build("vf_firsttask-frontend")
                    }
                }
            }
        }

        stage('Database Setup') {
            steps {
                script {
                    docker.image('mysql:8.0').withRun('-e MYSQL_ROOT_PASSWORD=rootpassword -e MYSQL_DATABASE=mydatabase -p 3306:3306') { c ->
                        // Wait for MySQL to start
                        sh "sleep 30"

                        // Execute SQL initialization script
                        docker.run("--rm --link ${c.id}:database -v ${WORKSPACE}/database/init.sql:/init.sql mysql:8.0 sh -c 'exec mysql -hdatabase -uroot -prootpassword mydatabase < /init.sql'")
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image('vf_firsttask-backend').withRun('-p 5000:5000 --link database:mysql') { c ->
                        // Wait for backend service to start
                        sh "sleep 30"

                        // Run backend tests (replace with actual test commands)
                        sh "docker exec ${c.id} pytest"  // Example command, replace with your actual test command
                    }

                    docker.image('vf_firsttask-frontend').withRun('-p 3000:3000 --link backend:backend') { c ->
                        // Wait for frontend service to start
                        sh "sleep 30"

                        // Run frontend tests (replace with actual test commands)
                        sh "docker exec ${c.id} npm test"  // Example command, replace with your actual test command
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                // Example deployment step (replace with your deployment process)
                script {
                    docker.image('vf_firsttask-backend').push('your-registry-url/vf_firsttask-backend')
                    docker.image('vf_firsttask-frontend').push('your-registry-url/vf_firsttask-frontend')
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker resources
            script {
                backendImage.remove()
                docker.image('vf_firsttask-frontend').remove()
                docker.image('mysql:8.0').stop()
                docker.image('mysql:8.0').remove()
            }
        }
    }
}

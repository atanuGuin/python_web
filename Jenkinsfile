def CONTAINER_NAME="portfolio"
def CONTAINER_TAG="latest"
// Update Docker hub User Account Details over here
def DOCKER_HUB_USER="atanu92"
def HTTP_PORT="80"
def STOP_C="docker ps -a -q"

node {

    stage('Checkout') {
    checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/atanuGuin/python_website.git']]])

    }

    stage("Remove stopped containers"){
        imagePrune(CONTAINER_NAME)
    }

    stage('Image Build, Multiple Tag'){
        imageBuild(CONTAINER_NAME, CONTAINER_TAG)
    }

    stage('Push to Docker Registry'){
        withCredentials([usernamePassword(credentialsId: 'dockerHubAccount', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
            pushToImage(CONTAINER_NAME, CONTAINER_TAG, USERNAME, PASSWORD)
        }
    }

    stage('Run App'){
        runApp(CONTAINER_NAME, CONTAINER_TAG, DOCKER_HUB_USER, HTTP_PORT)
    }

    stage('Run in GKE App'){
        runGKE()
    }
}

def imagePrune(containerName){
    try {
        echo "Removing unused containers :- "
        sh "docker stop $containerName"
        sh "docker system prune -f"
        sh "docker image prune -f"
        sh "docker container ls"
        
    } catch(error){}
}

def imageBuild(containerName, tag){
    echo "Images Present :- "
    sh "docker images"
    sh "docker build -t $containerName:$tag  -t $containerName ."
    sh "docker images"
    echo "Image build complete"
}

def pushToImage(containerName, tag, dockerUser, dockerPassword){
    sh "docker login -u $dockerUser -p $dockerPassword"
    sh "docker tag $containerName:$tag $dockerUser/$containerName:$tag"
    sh "docker push $dockerUser/$containerName:$tag"
    echo "Image push complete"
}

def runApp(containerName, tag, dockerHubUser, httpPort){
    sh "docker pull $dockerHubUser/$containerName"
    sh "docker run -d --rm -p $httpPort:5000 --name $containerName $dockerHubUser/$containerName:$tag"
    echo "Application started on port: ${httpPort} (http)"
}

def runGKE(){

    sh "kubectl apply -f yaml/python-app-deployment.yaml"
    sh "kubectl apply -f yaml/python-app-service.yaml"
    sh "kubectl get pods -o wide"
    sh "kubectl get services -o wide"
}
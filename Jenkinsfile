def CONTAINER_NAME="webapp"
def CONTAINER_TAG="latest"
def DOCKER_HUB_USER="atanu92"
def STOP_C="docker ps -a -q"

node {

    stage('Checkout') {
    checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/atanuGuin/python_web.git']]])

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
        runApp(CONTAINER_NAME, DOCKER_HUB_USER)
    }
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

def runApp(containerName, dockerHubUser){
    sh "docker pull $dockerHubUser/$containerName"
    echo "Kubernetes pods deployment starting..."
    sh "kubectl apply -f yaml/deployment.yaml"
    sh "kubectl get pods -o wide"
    sh "kubectl get services -o wide"

}

def CONTAINER_NAME="webapp"
def CONTAINER_TAG="latest"
def ECR_USER="595977377347.dkr.ecr.us-east-1.amazonaws.com"
def STOP_C="docker ps -a -q"

node {

    stage('Checkout') {
    checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/atanuGuin/python_web.git']]])

    }

    stage('Image Build, Multiple Tag'){
        imageBuild(CONTAINER_NAME, CONTAINER_TAG)
    }

    stage('Push to ECR Repository'){
            pushToImage(CONTAINER_NAME, CONTAINER_TAG, ECR_USER)
    }

    stage('Run App'){
        runApp(CONTAINER_NAME, ECR_USER)
    }
}

def imageBuild(containerName, tag){
    echo "Images Present :- "
    sh "docker images"
    sh "docker build -t $containerName:$tag  -t $containerName ."
    sh "docker images"
    echo "Image build complete"
}

def pushToImage(containerName, tag, ecrUser){
    sh "docker tag $containerName:$tag $ecrUser/$containerName:$tag"
    sh "docker push $ecrUser/$containerName:$tag"
    echo "Image push complete"
}

def runApp(containerName, ecrUser){
    sh "docker pull $ecrUser/$containerName"
    echo "Kubernetes pods deployment starting..."
    sh "kubectl apply -f yaml/deployment.yaml"
    sh "kubectl get pods -o wide"
    sh "kubectl get services -o wide"

}

#This is the scrpt to build the docker image for graphdb and push it to the github container registry

echo "<YOUR_GITHUB_TOKEN>" | docker login ghcr.io -u <YOUR_GITHUB_USERNAME> --password-stdin

docker tag graphdb-image:latest ghcr.io/circular-twain/ctontolib/graphdb-image:latest

docker push ghcr.io/circular-twain/ctontolib/graphdb-image:latest


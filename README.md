# Prediction API

## Docker Container 

This setup requires Docker to run on your PC. I've used Windows and Powershell or the terminal on Mac to run the commands. You can find the downloads for [Windows](https://www.docker.com/docker-windows) and [Mac](https://www.docker.com/docker-mac) at the respective links. 

The Create an image from the Flask service and run it and upload it as a web service, follow these steps:

### Build the image by running:
```docker
docker build -t <image-name> .
```

Where -t is used to set the tag for the image to create. The dot (.) at the end refers to the file path of the Dockerfile. For the build to work, the whole path can't contain any spaces. Something like C:\test would be fine, but "C:\test\this app" wouldn't be.

An example: 

```docker
docker build -t flask-rest .
```

### Run the container locally:
```docker
docker run -p 8000:8000 <image-name>
```

The property -p sets the port mapping for the container. As the script exposes port 8000, this should be mapped to another port of the container. You might change the second value (right) to change the port to speak to. 

An example: 

```docker
docker run -p 8000:8000 flask-rest
```

### **[Option 1/2]** Upload image to Docker Hub:

1. Login to docker from command line

    ```docker
    docker login --username <docker-id> --password <docker-hub-password>
    ```

    It is more secure, to use --password-stdin to login to your docker account:

    ```docker
    $ cat ~/my_password.txt | docker login --username foo --password-stdin
    ```

    More information can be found in the [Docker Docs](https://docs.docker.com/engine/reference/commandline/login/#parent-command)

2. Push the image to Docker Hub:
    ```docker
    docker push <docker-id>/<name-of-image>:v1.0.0 .
    ```

### **[Option 2/2]** Upload image to Azure Container Registry

0. Prepare for upload:

    ```shell
    pip install --user azure-cli
    ```
    
    If this doesn't work, download the installer and follow the instructions up on [Azure Docs](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)

1. Login to your container registry:

    ```docker 
    docker login <acr-name>.azurecr.io 
    ```

2. Push to your registry:

    ```docker 
    docker tag <image-name> <acr-name>.azurecr.io/<repo-name>
    docker push awesome.azurecr.io/<repo-name>
    ```

    More info in the [Azure Docs](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-docker-cli)

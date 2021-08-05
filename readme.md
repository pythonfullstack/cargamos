# FLASK REST API with FALSK-RESTX
----

## How to run the project
#### 1. Installation Docker and Docker compose
    sudo apt update -y
    suod apt install docker.io -y
    sudo apt install docker-compose -y
##### 2. Build Docker-compose and run

You can just run the following bash file

    ./run_docker.sh

**_Note_:** If you encountered permission problem, you can run the following command before the above command
   
    chmod +x run_docker.sh

## How to check the result
> **Swagger Document URL**: [server URL]/api/v1
> 
> **Celery Result by Flower**: port: 5557
> 
## Available Features
**Note:** The following features haven't been implemented yet.
>1. Load-balancing with Nginx
>2. Continues Integration
>3. Continues Deployment with K8s
>4. Load-balancing with K8s


## Tips:
**Tech-stacks used:**
> 1. Flask, Asynchronous tasks with Celery, threading
> 2. PostgreSQL, Redis   
> 3. Nginx
> 4. GitHub Actions for CI with testing
> 5. Docker, bash-script

**For Your Information, Initial DB migration**

You should run the following commands to migrate Database on another terminal after running docker images
    
    sudo docker-compose exec web sh
----
    flask db init
    flask db migrate
    flask db upgrade

#### **Note:** Please make sure you copied env file.
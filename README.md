# Restaurant app

#####

Description: this is a simple http application using Flask that provides insights on restaurant data

### Installation

#### 1. Install the dependencies:

```
pip install -r requirements.txt
```

##### This will install the dependencies needed to run the application

#### 2. Run the application

```
python main.py
```

##### This will run the applicaton locally on port 5000 (http://127.0.0.1:5000/)

#### 3. Deployment
##### Once you have confirmed that the application runs successfully locally, you can now build a container image via docker:

```
docker build -t restaurant-app:latest .
```

##### run the container to see if it is working

```
docker run -p 4000:80 restaurant-app:latest
```

##### check on http://localhost:4000/ to see if the container is running
###### Do note that Port 80 is the port exposed on the docker container which we will bind to 4000 on the local machine

&nbsp;
### A short summary on how i would design and deploy this app using cloud services and my decisions and considerations i have made when designing the solution. 

I would deploy this on a cloud platform using a server architecture due to the higher performance it provides. While a serverless architecture would be better for scaling fast if there are a high concurrent number of users, I do not see any reason if the main purpose of this application is for downloading and viewing data, there may not be a need for rapid scaling. 

Before deploying on a server, I would have to build a container to ensure that the versions of the dependencies are consistent and that it can be used to run on any machine.

Furthermore, a serverless architecture also has an issue with cold starts, where it will take a longer period of time to pull data from the container registry and start the program, given that the container has extremely huge resources, the datasets, it would not be wise to rely on a serverless architecture as it will take a way longer time to pull the container from the container registry and start the container.
One of the key benefits of using a container instead of a virtual machine is that it would allow me to cut down server resources and minimise cost, since I do not have to run a full operating system on the server when I host.

In the event that there is significantly high traffic and that upgrading a server may be more costly through vertical scaling, I can switch up and add a load balancer to distribute the workload across multiple servers or use cloud orchestration tools such as Kubernetes to scale horizontally.


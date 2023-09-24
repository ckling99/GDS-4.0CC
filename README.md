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

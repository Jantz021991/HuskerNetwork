# HuskerNetwork  
---------------------------------------------------------------------------------------------------------
<div style="text-align:center">
<img src="https://github.com/Jantz021991/HuskerNetwork/blob/master/HuskersNetwork.JPG" width="800" height="200" />
                                                                                                               </div>


This repository is being built as part of our class - Enterprise Architecture and Systems Integration -Batch:Spring 2018, Management Information Systems - University of Nebraska at Omaha.

The repository includes code to build a social networking website.

Collaborators to build this application by integrating Program Interfaces are -

* Narahari Sundaragopalan
* Vivek Bhat Hosmat
* Vaibhav Rahangdale
* Erdenebileg Bat-Erdene
* Deepika Jantz


## Instructions for local environment setup

### Using Virtual Env

* Create a virtual environment using the command
  ```
      virtualenv -p python3 <yourEnvNameHere>
  ```

    *Do not push your local virtual environment to github repo. Create the virtual environment in a separate folder outside the repo*

* Activate your virtual environment using
```
      source <pathToYourVirtualEnv>/bin/activate
```
* Install Packages using
```
      pip -r requirements.txt
```
    *If you have new packages to install, add them in the requirements.txt file and push that file to the repo*

* Run the migrations using below command from the root folder of your repo
```
      python manage.py migrate
```
* To access the application on http://localhost
```
      python manage.py runserver
```


### Using Docker Containers

> Another alternative to virtual environment is using Docker containers. See below instructions for setup

* From the root directory, run the following command to create a persistent storage for postgres database container. This way the data will persist and we don't have to run django migrations and create a superuser every time we work on it.
      docker volume create --name postgres-data

* Once the volume is created, you can start the Docker containers using
```
    docker-compose up -d
```

* Once the containers are running, to run the database migrations, use the command
```
      docker-compose run web python manage.py migrate
```

* To create a super user, use
```
      docker-compose run web python manage.py createsuperuser
```

* If you do not want to run your Docker containers all the time, you can stop the containers using
```
      docker-compose down
```

When you need to run any command with ```manage.py``` during development, you need to preface the ```python manage.py [command]``` with ```docker-compose run web```. This tells Docker to run the command on the web container, which is our main Django App container

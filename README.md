# Flask_REST_API_with_Docker

#Install docker

Install docker in windows it can be done by installing exe directoly into windows and following the next button and finish.
next configer docker with desktop.

# Files
In here i have two directory one with name Screen_files it contain screen sorts of folder or directory how i have files in my working directory.
another is my working directory name where i keep all files including sqlite3 database.

Taka    

--db

    |--GDT.db

|-- templets

    |-- addnew

    |-- del_sub

    |-- delete

    |-- home

    |-- list

    |-- result

|-- app.py

|-- docker-compose.yml

|-- Dockerfile

|-- requirements.txt


# About files 

* db folder contains database file
* templets folder contains .html files 
* and rest are docker files and requirement text file 
* last app.py file which have main codes 

-- requirement.txt file tells python everything it will need to run our app.

# The Docker

Docker is going to take the place of our usual physical system, so we will start there. I’m using a base docker image based on alpine – a lightweight docker image.

We then just need to do some other set up work:

copy the directory containing the docker image into ‘/app’ inside the container so the container has access to the project.
Set the working directory to be the correct directory within app.
Run pip install with the requirements.txt file inside this working directory.

FROM python:3.8

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]

docker-compose.yml

This file is basically the backbone as it contains all the information needed to run the desired services.
Docker compose is primarily a way for controlling multi-container builds, but we can use it here to encapsulate some of our configuration.

version: "3.7"

services:
  taka:
    build:
      context: ./
    ports:
      - 5000:5000

# launch docker 
go to the directory where you have all project in my case c:/Users/<username>/Documents/<filename>/
launch command prompt and make sure you are in right directory. 

issue the command 

docker-compose up

now your system will create a docker container and you will abel to see the image name in docker desktop application which installed before.
all results images are in result folder

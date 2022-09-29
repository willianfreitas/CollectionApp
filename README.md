# CollectionApp
A simple project with Insert, Update and Delete functions.

## Introduction

After clone, you need to run the following command:
  ```bash
  docker-compouse up
  ```
  
  ### Create User
  
  To create the first user, enter on container and run:
  ```
  python3 manage.py createsuperuser
  ```
  
  After create the superuser, you i'll able to create your token access, in POST endpoint:
  ```
  localhost:8000/token/
  ```
  with this params:
  ```
  {
    "username":{username},
    "password":{password}
  }
  ```
  The post will return a json with access token called "acess" and "refresh":
  ```
  {
    "refresh":"...",
    "acess":"..."
  }
  ```
  You will uses the token as bearer token in each requisition as Autorization.
  
  ### Swagger
  All endpoint documentation you will find in:
  ```
  localhost:8000/docs/
  ```

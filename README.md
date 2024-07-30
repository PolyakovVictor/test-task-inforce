## Project deployment


#### Need to create an .env file in the root path '/' along with docker-compose.yml:
```plaintext

Example .env file

POSTGRES_DB=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

#### Build and run Docker containers:

```sh
docker-compose up --build -d
```
#### Test api
you can get into the docker container using 
```sh
docker exec -it test-task-inforce_app_1 /bin/sh
```
and run the command

```sh
python manage.py create_test_data
```
to create the test information

#### main urls
To receive a token.
```sh
/token/
```
To create a new user (employee).
```sh
/employees/
```
To add a restaurant and view restaurants.
```sh
/restaurants/
```
To add and view menus.
```sh
/menus/
```
To vote for the menu.
```sh
/votes/
```

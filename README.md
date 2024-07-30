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

# test_app_api

To launch this project locally first you need to add .env file with something like this in it:
```
DEBUG=0
SECRET_KEY=secret
DATABASE_URL=psql://postgres:postgres@db:5432/postgres
```

then just execute these two commands:
```
docker-compose build
docker-compose up
```

Launch tests using ```pytest``` while in project directory

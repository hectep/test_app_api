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

#API documentation:
For detailed version refer to api-documentation.html
- POST, GET: ```/api/app/```

creates new app and retrieves list of apps

- GET, DELETE, PUT: ```/api/app/<int:pk>/```

GET retrieves app object, PUT updates name of an app object

- PUT: ```/update_key/<int:pk>/```

regenerates api-key of an app and returns new api-key

- GET ```test/<str:api_key>/```

retrieves app object by api-key

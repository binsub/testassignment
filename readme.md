# Backend for handling cab trip

### Deployment

#### To build the docker container
```
docker build -t istart .
```
#### To build the docker container
```
docker run -p 8080:8080 istart
```

### Endpoints
http://localhost:8000/api/v1/trip [GET, POST, PUT, DELETE]

Make sure request the api with basic auth as authorization, password is at account_credentials.json

### Dependencies
- [Flask](https://www.palletsprojects.com/p/flask/).
- [pytest](https://docs.pytest.org/en/latest/) for testing
- [Marshmallow](https://marshmallow.readthedocs.io/en/stable/) for Validation, Serialization and Deserialization
- [SQLAlchemy](https://www.sqlalchemy.org/) for ORM.
- [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Docker](https://www.docker.com/products/docker-desktop)

### IDE
Please use [Visual Studio Code](https://code.visualstudio.com/)
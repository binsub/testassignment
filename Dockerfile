FROM python:3.7-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk add --no-cache build-base libffi-dev mariadb-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY istart_app istart_app
COPY main.py test.db config.py credentials.py account_credentials.json ./

EXPOSE 8080
CMD ["python", "main.py"]

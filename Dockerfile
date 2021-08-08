FROM python:3.9

WORKDIR /app

COPY Pipfile* .

RUN pipenv install

COPY . .

# hostport:internal-container-port
EXPOSE 8000:8000

CMD ["python", "manage.py", "runserver"]
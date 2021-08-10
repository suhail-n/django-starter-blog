# django-starter-blog

> Build a simple blog using django rest framework

## Run Dev

> docker compose devmode is currently not working
### Docker Compose

1. `docker-compose up --build`
2. navigate to `localhost:8000` for django rest framework API navigation
3. navigate to `localhost:8000/admin` for admin site
4. superuser `username:password -> admin:admin`

### Manual

1. `pip install pipenv`
2. `pipenv install`
3. `pipenv run python manage.py migrate`
4. `pipenv python manage.py createsuperuser` create new super user 
5. `pipenv run manage.py`
6. navigate to `localhost:8000/admin` for admin site
7. superuser `username:password -> admin:admin`

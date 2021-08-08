FROM python:3.9

WORKDIR /app

COPY Pipfile* .

RUN pip install pipenv && \
    pipenv install

COPY . .

EXPOSE 8000

CMD ["pipenv", "run", "startdev"]
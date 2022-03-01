FROM python:3.8

COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install

EXPOSE 5000
ENTRYPOINT [ "pipenv" ]
CMD ["run", "gunicorn", "--workers=4", "--bind=0.0.0.0:5000", "app:my_app"]

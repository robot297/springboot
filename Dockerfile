FROM python:3.8 AS flask_builder

COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install
RUN pipenv run python setup.py bdist_wheel

FROM python:3.8 AS flask_app

COPY --from=flask_builder /app/dist/. /app

RUN pip install /app/api_demo-1.0.0-py3-none-any.whl
RUN pip install waitress
WORKDIR /app

EXPOSE 8080

CMD ["waitress-serve", "-call", "api-demo:create_app"]

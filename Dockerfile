FROM python:3.8

COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install

EXPOSE 5000

CMD ["pipenv", "run", "python", "app.py"]

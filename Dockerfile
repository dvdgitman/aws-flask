FROM python:3

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

ENTRYPOINT flask run
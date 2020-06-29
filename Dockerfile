FROM python:3

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY /src .

CMD flask run --host=0.0.0.0 --port=5000
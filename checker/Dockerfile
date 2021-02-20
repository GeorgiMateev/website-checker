FROM python:3.9-buster
RUN apt-get clean \
    && apt-get -y update

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt --src /usr/local/src

COPY src/ ./src/

CMD ["python3","-u","src/main.py"]
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP wsgi.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
COPY . .
CMD ["flask", "run"]

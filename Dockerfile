FROM python:3.9.6-alpine

# set work directory
WORKDIR /srv/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 and Pillow dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev \
    && apk add git cmake make gettext-dev libintl  # for locales

# install locale
RUN cd /tmp && git clone https://github.com/rilian-la-te/musl-locales.git
RUN cd /tmp/musl-locales && cmake . && make && make install

ENV LANG=ru_RU.UTF-8 \
    LANGUAGE=ru_RU.UTF-8

# install dependencies
RUN pip install --upgrade pip
COPY ./src/requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ./src/ .

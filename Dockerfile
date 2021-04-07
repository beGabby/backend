FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

RUN echo http://nl.alpinelinux.org/alpine/v3.9/main > /etc/apk/repositories; \
    echo http://nl.alpinelinux.org/alpine/v3.9/community >> /etc/apk/repositories

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN adduser -D user
USER user
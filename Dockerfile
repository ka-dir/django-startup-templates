###########
# BUILDER #
###########

# pull official base image
FROM python:3.10-slim as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get -y install libpq-dev gcc python3-dev default-libmysqlclient-dev build-essential

# lint
RUN pip install --upgrade pip
RUN pip install black
COPY . .
RUN python -m black .
# install dependencies
RUN pip freeze > ./requirements.txt
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.10-slim

# create directory for the app user
RUN mkdir -p /home/app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles

WORKDIR $APP_HOME

# install dependencies
RUN apt-get update && apt-get -y install libpq-dev gcc python3-dev default-libmysqlclient-dev build-essential
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache /wheels/*

EXPOSE 3000

# copy project
COPY . $APP_HOME

RUN chmod 0755 $APP_HOME/ -R

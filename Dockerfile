FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code;
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update -y \
&& apt-get upgrade -y pip \ 
&& pip install --upgrade pip \
&& pip install -r requirements.txt
COPY . /code/
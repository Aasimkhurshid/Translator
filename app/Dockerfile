# syntax=docker/dockerfile:1
FROM python:3.7-slim-buster 
RUN apt-get update
RUN apt-get upgrade -y
COPY ./ /app/
WORKDIR /app
RUN pip install -r requirements.txt
CMD python main.py
# EXPOSE 3000
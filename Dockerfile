FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
RUN echo "from HBDU import *" > /app/main.py
COPY ./src/HBDU /app/HBDU/

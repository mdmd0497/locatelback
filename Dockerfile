FROM python:3.9-bullseye

WORKDIR /usr/src/app

ADD ./requirements.txt /usr/src/app


#RUN pip install -r requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

ADD . /usr/src/app

EXPOSE 5003

CMD ["uvicorn", "config:app", "--host=127.0.0.1", "--port=5003"]
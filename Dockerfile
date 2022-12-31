FROM python:3.9-bullseye

WORKDIR /usr/src/app

ADD ./requirements.txt /usr/src/app


#RUN pip install -r requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

ADD . /usr/src/app

EXPOSE 80

CMD ["uvicorn", "config:app", "--host=0.0.0.0", "--port=80"]
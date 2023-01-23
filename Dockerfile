FROM python:3.9-bullseye

WORKDIR /usr/src/app

COPY . .

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="${PATH}:/root/.local/share/pypoetry/venv/bin/"
RUN ["poetry", "install", "--no-dev"]

EXPOSE 5003

CMD ["poetry", "run", "start"]
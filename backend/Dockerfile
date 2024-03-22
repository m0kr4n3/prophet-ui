FROM ubuntu:latest

RUN apt-get update -y && apt-get upgrade -y

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends   python3.11 python3-pip libpq-dev python3-psycopg2 python3-dev

RUN python3 --version

RUN apt-get install -y python3-psycopg2

RUN mkdir /api

WORKDIR /api

COPY backend/requirements.txt ./

RUN pip3 install -U pip

RUN pip3 install psycopg2

RUN pip3 install -r requirements.txt

COPY backend/ ./

EXPOSE 5000

RUN useradd -ms /bin/bash api

RUN chown -R api:api /api

USER api

ENTRYPOINT ["python3", "-m", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
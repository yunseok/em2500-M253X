FROM python:3.8
MAINTAINER Alan <contact@yunseok.dev>

WORKDIR /em2500-M253X
COPY . /em2500-M253X

RUN pip install --no-cache-dir -r requirements.txt

CMD python index.py

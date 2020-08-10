FROM python:3.8
MAINTAINER Alan <contact@alan-web.dev>

WORKDIR /em2500-M253X
COPY . /em2500-M253X

RUN pip install --no-cache-dir -r requirements.txt

CMD python main.py
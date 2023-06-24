FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY server/requirements.txt /code

RUN pip install -r requirements.txt

COPY server /code

COPY docker-entrypoint.sh /

CMD ["sh", "/docker-entrypoint.sh"]

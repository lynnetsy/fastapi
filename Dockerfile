FROM python:3.11.6-alpine3.18

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update \
    && apk add --no-cache \
        build-base \
        postgresql-dev \
        python3-dev

COPY . .

RUN pip install app

CMD ["tail", "-f", "/dev/null"]
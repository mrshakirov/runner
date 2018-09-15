FROM python:3.6-alpine
ENV PYTHONPATH=${PYTHONPATH}:/app
RUN apk add --no-cache gcc make libc-dev
WORKDIR /app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./app ./

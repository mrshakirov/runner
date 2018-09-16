FROM python:3.6
ENV PYTHONPATH=${PYTHONPATH}:/app
WORKDIR /app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./app ./

FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir -p /var/www/website/html
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD ./sp_test /code/

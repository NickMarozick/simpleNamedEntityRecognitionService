FROM python:3.7

RUN pip3 install gevent

EXPOSE 8080
COPY requirements.txt ./requirements.txt
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . .

CMD python3 rest.py

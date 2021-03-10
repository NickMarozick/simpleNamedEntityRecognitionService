FROM python:3.7

RUN pip3 install gevent

EXPOSE 8080
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY . .

CMD python3 server.py

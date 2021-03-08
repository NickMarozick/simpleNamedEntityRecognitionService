FROM python:3.7

EXPOSE 8501

WORKDIR /streamlit-docker

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD streamlit run simpleUI.py --server.port 8081 --server.address 0.0.0.0

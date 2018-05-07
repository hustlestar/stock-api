FROM python:2.7.14

#RUN apt-get update \
#&& apt-get install -y wget
#RUN wget

WORKDIR /home/jack/

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

WORKDIR /home/jack/api

CMD ["python", "main.py"]
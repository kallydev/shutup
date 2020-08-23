FROM python:3.8-alpine

WORKDIR /root/shutup

ADD . .

RUN pip install -r requirements.txt

EXPOSE 443

ENTRYPOINT ["python", "app.py"]

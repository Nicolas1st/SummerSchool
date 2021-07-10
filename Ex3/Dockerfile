FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["find_bright_spot.py"]
ENTRYPOINT ["python3"]

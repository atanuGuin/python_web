# Docker file for Image Deployment
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev-is-python3 build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["python", "main.py"]

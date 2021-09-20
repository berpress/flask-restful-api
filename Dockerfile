FROM ubuntu:focal
MAINTAINER Alexander Litovsky 'berpress@gmail.com'
RUN apt-get update && apt-get install -y python3 python3-pip && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1 && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3 1
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python app.py

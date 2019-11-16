FROM ubuntu:18.04
MAINTAINER Lumir Jasiok "lumir.jasiok@alfawolf.eu"

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential \
    python3-pip

WORKDIR /app

RUN mkdir -p /var/log/hejtado/ && chown www-data: /var/log/hejtado/
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt --src /usr/local/src

COPY hejtado /build/hejtado
COPY MANIFEST.in /build/
COPY setup.py /build/
COPY README.rst /build/

RUN cd /build && /usr/bin/python3 setup.py install

COPY deploy/startup.sh /app/startup.sh
COPY deploy/nginx.conf /etc/nginx
COPY deploy/wsgi.py /app
COPY deploy/gunicorn.conf.py /etc

RUN chmod +x ./startup.sh

EXPOSE 80

CMD [ "./startup.sh" ]

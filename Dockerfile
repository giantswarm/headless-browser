FROM python:3.7-alpine3.12

# RUN echo "http://dl-4.alpinelinux.org/alpine/v3.11/main" >> /etc/apk/repositories && \
#     echo "http://dl-4.alpinelinux.org/alpine/v3.11/community" >> /etc/apk/repositories && \
#     apk update && \
#     apk --no-cache add chromium chromium-chromedriver python3-dev build-base git py3-lxml libxml2 libxml2-dev libxslt libxslt-dev libffi-dev openssl-dev && \
#     pip3 install --upgrade pip && \
#     pip3 install -r requirements.txt && \
#     apk del python3-dev build-base

RUN apk update
RUN apk --no-cache add chromium chromium-chromedriver

ADD requirements.txt /
RUN pip3 install -r requirements.txt

ADD examples /examples

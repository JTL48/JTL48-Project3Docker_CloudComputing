FROM alpine:latest

RUN apk add --no-cache python3
RUN apk add --no-cache dos2unix
RUN rm -rf /var/cache/apk/*
WORKDIR /home
RUN mkdir /home/data
RUN mkdir /home/output
COPY ./*.py .
COPY ./*.sh /usr/local/bin
RUN dos2unix /usr/local/bin/*.sh
CMD ["run.sh"]
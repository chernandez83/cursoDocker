FROM ubuntu
RUN mkdir /app
RUN cd /app && touch data.txt
COPY ./src/index.html /app/src/com/hola.html
COPY ./src /app/src_copy
ADD  file.tar.gz /com/src
ENV USER Batman
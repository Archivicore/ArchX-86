# We're using Ubuntu 20.10
FROM archivicore/archx-beta:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/archivicore/archx-beta /home/archivicore/
RUN mkdir /home/archivicore/bin/
WORKDIR /home/archivicore/

CMD ["python3","-m","userbot"]

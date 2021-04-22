# We're using Ubuntu 20.10
FROM Archivicore/ArchX:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/Archivicore/ArchX /home/Archivicore/
RUN mkdir /home/Archivicore/bin/
WORKDIR /home/Archivicore/

CMD ["python3","-m","userbot"]

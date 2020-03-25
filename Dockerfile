FROM ubuntu:18.04

COPY . /home/
WORKDIR /home/
RUN chmod 775 ./scripts/*.sh
RUN ./scripts/before_installation.sh
RUN ./scripts/installation.sh
ENTRYPOINT ["./venv/bin/python3", "app.py"]
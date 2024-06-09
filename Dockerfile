FROM python:3.10-slim

COPY . /sspr
WORKDIR /sspr

RUN pip3 install --upgrade pip
RUN pip3 install -e . --no-cache-dir

ENTRYPOINT [ "sspr" ]

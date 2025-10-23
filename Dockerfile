FROM python:3.10

RUN pip install tccli

ENTRYPOINT ["/usr/local/bin/tccli"]

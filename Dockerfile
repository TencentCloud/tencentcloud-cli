FROM python:3

RUN pip install tccli

ENTRYPOINT ["/usr/local/bin/tccli"]
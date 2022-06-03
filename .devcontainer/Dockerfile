FROM python:3.9

ARG OPENJDK_VARIANT=11
RUN apt-get update && \
    apt-get install -y openjdk-${OPENJDK_VARIANT}-jre-headless && \
    apt-get clean;

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir \
   install -r /tmp/pip-tmp/requirements.txt && rm -rf /tmp/pip-tmp

ENV SPARK_HOME="/usr/local/lib/python3.9/site-packages/pyspark"
ENV PYTHONUNBUFFERED=1

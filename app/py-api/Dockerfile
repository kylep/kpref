FROM ubuntu:focal
ADD image-files/ /
RUN apt-get update \
 && apt-get install -y \
      python3-pip
ADD app /app
CMD tail -f /dev/null
RUN pip install /app tox
CMD /start.sh

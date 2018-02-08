# A simple Flask app container.
FROM python:2.7
LABEL maintainer="None"

# Place app in container.
COPY app /opt/www
WORKDIR /opt/www

# Install dependencies.
RUN pip install -r requirements.txt

EXPOSE 5000
CMD python index.py

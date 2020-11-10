FROM python:3.8-alpine

# To enable logging
ENV PYTHONUNBUFFERED 1

# Create server directory
RUN mkdir -p /backend/project

WORKDIR /backend/project

# Install the dependencies
COPY requirements.txt /backend/project

ADD . .

RUN pip3 install -r requirements.txt

# Bundle the source
COPY . /backend/project

EXPOSE 8000
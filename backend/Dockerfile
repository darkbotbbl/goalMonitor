FROM python:3.8.6-slim-buster

# To enable logging
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create server directory
RUN mkdir -p /backend/project

WORKDIR /backend/project

# Install netcat
RUN apt-get update && apt-get install -y netcat 

ADD . .

# Install the dependencies
RUN pip install --upgrade pip

COPY requirements.txt /backend/project

RUN pip install -r requirements.txt


# Copy the entrypoint
COPY entrypoint.sh /backend/project

# Bundle the source
COPY . /backend/project

EXPOSE 8000

# Run the entrypoint.sh as the entrypoint script
ENTRYPOINT ["/backend/project/entrypoint.sh"]

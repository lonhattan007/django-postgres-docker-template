# Pull base image
FROM python:3.8-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY ./requirements.txt .
RUN apt-get update && \
	apt-get install -y libpq-dev gcc
RUN pip install -r requirements.txt

# Copy project
COPY . .

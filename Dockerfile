# Pull base image
FROM python:3.9

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /src/

# Install dependencies
RUN pip install -r requirements.txt
# RUN pipenv install --system --dev

COPY . /src/

EXPOSE 8000
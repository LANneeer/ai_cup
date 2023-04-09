FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update \
  && apt-get install -y --no-install-recommends apt-utils \
  && apt-get install -y --no-install-recommends libc-dev \
  && apt-get install -y --no-install-recommends gcc \
  && apt-get install -y --no-install-recommends gettext \
  && apt-get install -y --no-install-recommends screen \
  && apt-get clean


WORKDIR /app

# Copy project
COPY README.md README.md
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
COPY hackathon ./hackathon

RUN pip install poetry
RUN poetry install --only main
RUN poetry build

# Expose ports
EXPOSE 8000 3001

# Run the command to start the server
CMD ["sh", "-c", "poetry run hackathon/manage.py runserver 0.0.0.0:8000 & poetry run hackathon/manage.py runbot 0.0.0.0:3001"]

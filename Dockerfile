FROM python:3.9-alpine
WORKDIR /apps/verdant/
COPY src/verdant/. .
COPY requirements/development.txt .
RUN ["pip", "install",  "--no-cache-dir", "-r", "development.txt"]
CMD ["python", "verdant.py"]

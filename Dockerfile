FROM python:3.12-slim

WORKDIR /usr/src/app

# deps
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

# código
COPY . .

EXPOSE 80
CMD ["fastapi", "main:app", "--host", "0.0.0.0", "--port", "80"]

FROM python:3.12-slim
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80
CMD ["fastapi", "dev", "--host", "0.0.0.0", "--port", "80", "main.py"]

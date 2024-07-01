FROM python:3.9-slim
WORKDIR /app
COPY . .
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]


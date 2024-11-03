FROM python:3.9-slim
WORKDIR /app
COPY . .
EXPOSE 6000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]


FROM public.ecr.aws/docker/library/python:3.11-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir flask
EXPOSE 5000
CMD ["python", "main.py"]

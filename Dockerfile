# Usa una imagen base liviana de Python
FROM python:3.11-slim

# Establece directorio de trabajo
WORKDIR /app

# Copia todos los archivos del repo al contenedor
COPY . /app

# Instala Flask
RUN pip install --no-cache-dir flask

# Expón el puerto que usará Flask
EXPOSE 5000

# Ejecuta tu app
CMD ["python", "main.py"]

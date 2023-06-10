# Usa la imagen base de Python
FROM python:3.11.3

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de tu proyecto al directorio de trabajo
COPY src/ /app/src
COPY requirements.txt requirements.txt

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Establece el comando predeterminado para ejecutar tu aplicación
CMD ["python", "src/app.py"]

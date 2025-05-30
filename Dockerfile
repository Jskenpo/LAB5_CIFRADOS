# Usa una imagen oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de la app a /app
COPY main.py .

# Instala Streamlit
RUN pip install --no-cache-dir streamlit

# Expone el puerto usado por Streamlit
EXPOSE 8501

# Comando por defecto para iniciar la app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
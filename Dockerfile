# Base image
FROM python:3.9

# Çalışma dizini
WORKDIR /app

# Gerekli dosyaları kopyalama
COPY . .

# Uygulamayı kurma
RUN pip install -r requirements.txt

# Uygulamayı başlatma
CMD ["python", "app.py"]

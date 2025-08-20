# 1. Bazowy obraz Pythona
FROM python:3.9-slim

# 2. Katalog roboczy w kontenerze
WORKDIR /app

# 3. Instalacja zależności
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kopiowanie całego projektu
COPY . .

# 5. Uruchomienie API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Используем минималистичный образ Python
FROM python:3.11-alpine

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем список зависимостей
COPY requirements.txt .

# Устанавливаем библиотеки без сохранения кэша для уменьшения размера образа
RE RUN pip install --no-cache-dir -r requirements.txt

# Копируем основной код бота
COPY main.py .

# Запускаем скрипт с флагом -u для корректного отображения логов в Docker
CMD ["python", "-u", "main.py"]

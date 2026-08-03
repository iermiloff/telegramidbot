# Telegram Media ID Bot 🤖

Простой и легковесный Telegram-бот внутри Docker, который возвращает `file_id` любого отправленного или пересланного ему медиафайла. Позволяет копировать ID в один клик.

## Поддерживаемые типы медиа
* 🖼️ Фотографии (`photo`)
* 🎬 Видео (`video`)
* 🔄 GIF-анимации (`animation`)
* 🎵 Аудиозаписи (`audio`)
* 🎙️ Голосовые сообщения (`voice`)
* 📹 Кругляшки / Видеосообщения (`video_note`)
* 📁 Любые документы и файлы (`document`)

---

## 🚀 Быстрый запуск на сервере

### 1. Подготовка окружения
Склонируйте репозиторий на свой сервер и перейдите в папку проекта:
```bash
git clone https://github.com/iermiloff/telegramidbot/
cd telegramidbot/
```

### 2. Настройка токена
Создайте файл `.env` в корневой директории:
```bash
nano .env
```
Добавьте в него ваш токен от `@BotFather`:
```env
BOT_TOKEN=1234567890:ABCdefGhIJKlmNoPQRsTUVwxyZ
```

### 3. Запуск в Docker
Запустите контейнер в фоновом режиме:
```bash
docker compose up -d --build
```

---

## 🛠️ Полезные команды

* **Просмотр логов бота:**
  ```bash
  docker compose logs -f tg_media_id_bot
  ```
* **Остановка бота:**
  ```bash
  docker compose down
  ```
* **Перезапуск контейнера:**
  ```bash
  docker compose restart tg_media_id_bot
  ```

---
## Технологический стек
* **Язык:** Python 3.11 (Alpine)
* **Библиотека:** pyTelegramBotAPI
* **Окружение:** Docker / Docker Compose

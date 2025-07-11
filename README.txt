📦 FBaking Telegram Bot (тестовая версия)

🔧 Установка и запуск на Render:

1. Перейди на https://dashboard.render.com
2. Нажми "New" → "Web Service"
3. Залей архив или подключи GitHub
4. Укажи:
   - Build Command: pip install -r requirements.txt
   - Start Command: python3 main.py
5. В разделе Advanced → Instance Type выбери "Background Worker"
6. Нажми "Create Web Service"

Бот будет работать в режиме polling.

Токен уже встроен в main.py. В любой момент можно заменить.

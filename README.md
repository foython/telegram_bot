========================================================
Django DRF Project with Telegram Bot and Celery
========================================================

This project is a Django application using Django REST Framework, Celery, and Telegram Bot API. It provides public and protected APIs, processes background tasks using Celery, and integrates a Telegram bot to collect usernames.

*** I forgot to commit it from very beginning so my first commit was after celery integration ***
------------------------------
1. Project Setup
------------------------------
- Django project is configured for production use.
- Environment variables are used for:
    - `SECRET_KEY`
    - EMAIL_HOST_USER
    - EMAIL_HOST_PASSWORD
    - TELEGRAM_BOT_TOKEN

Settings:
- DEBUG = False 
- Use `.env` file or system environment variables

Install dependencies:
    pip install -r requirements.txt

Run migrations:
    python manage.py migrate

------------------------------
2. API Endpoints
------------------------------

✅ Public API:
    Method: GET  
    URL:    http://localhost:8000
    Description: Accessible without authentication.

✅ Protected API:
    Method: GET/POST/put/delete 
    URL:    http://localhost:8000/user
    Auth:   JWT Authentication
   **only post request public others protected**

✅ API login:
    URL: http://localhost:8000/account/api/login 
    Auth: JWT Authentication
    
✅ Web login:
    URL: http://localhost:8000/account/login 
    Uses standard Django admin/login flow.

------------------------------
3. Celery Integration
------------------------------

- Broker: Redis  
- Start Redis server locally or via Docker

Start Celery worker:
    celery -A telegram_bot worker --loglevel=info

Example Task:
- Greetings email is sent after user registration.

------------------------------
4. Telegram Bot Integration
------------------------------

Steps:

1. Find the bot name 'crop user data'.
2. run bot.py file from the project.   

Behavior:
- When a user sends `/start` to the bot:   
    - User's  `username` are saved to the database
    - For api key please contact me @ +8801629992299. 

------------------------------
5. Running the Project
------------------------------

Start Django server:
    python manage.py runserver

Start Celery worker:
    celery -A <your_project_name> worker --loglevel=info
    
Run bot.py file


------------------------------
6. Additional Notes
------------------------------

- Ensure required environment variables are loaded before running in production.
- `requirements.txt` includes all necessary dependencies (Django, DRF, Celery, Redis, etc.)
- Telegram usernames are collected only via `/start` command and stored uniquely by `username`.


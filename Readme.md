# Django-проект: Форум

## Стек технологий

- Python 3.10+
- Django 4.x
- SQLite (встроенная БД)
- Bootstrap 5 (для базовой вёрстки)
- Git (для контроля версий)
- HTML, шаблоны Django

---

## Как запустить проект

1. **Клонируй репозиторий:**

```bash
git clone https://github.com/ТВОЙ-ЮЗЕРНЕЙМ/название-репозитория.git
cd название-репозитория
```

**Создай виртуальное окружение и активируй его (если опять снес винду и берешь файлы с удаленного сервера):**
``` bash
python -m venv venv
# Windows
venv\Scripts\activate
```

2. **Выполни миграции:**

``` bash
python manage.py makemigrations
python manage.py migrate
```

Создай суперпользователя (Один раз, когда только создал бд):
``` bash
python manage.py createsuperuser
```

3. **Запусти сервер:**
``` bash
python manage.py runserver
```

--- 

 - **Полезные команды Git**
Основные:
``` bash
git status           # посмотреть состояние
git pull             # забрать последние изменения
git add .            # добавить все изменения
git commit -m "..."  # закоммитить изменения, вместо ... - опиши изменения которые сделал
git push             # отправить изменения на GitHub
``` 

 -  **Работа с pull request:** 

Сделай `git pull`, чтобы получить мои изменения.

Исправь конфликты (если будут).

Запушь обратно: `git push`.

 Работа с базой данных
```bash
python manage.py makemigrations   # создание миграций
python manage.py migrate          # применение миграций
python manage.py createsuperuser  # создать админа
```

База данных по умолчанию — db.sqlite3, она хранится в корне проекта.

🌐 Админка Django
URL: http://127.0.0.1:8000/admin/

Вход по логину, созданному через createsuperuser.
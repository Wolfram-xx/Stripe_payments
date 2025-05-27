# StripePayments Django App

Django-проект с интеграцией Stripe Checkout и Docker.

Из ТЗ не сделано:

Реализовать не Stripe Session, а Stripe Payment Intent. (не разобрался в документации)

Мог накосячить с Docker, так как имею мало опыта работы с ним

Адрес сервера - http://103.71.21.184:8000/

Данные админки внизу


---

## Описание

Проект представляет собой Django-приложение с функционалом оформления заказов и оплатой через Stripe Checkout.  

Для удобства разработки и деплоя проект упакован в Docker-контейнер.

---

## Установка и запуск локально

1. Клонируйте репозиторий:

```bash
git clone https://github.com/ТВОЙ_ЮЗЕРНЕЙМ/ТВОЙ_РЕПОЗИТОРИЙ.git
cd ТВОЙ_РЕПОЗИТОРИЙ
```
Создайте виртуальное окружение и установите зависимости:

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```
Создайте .env файл с переменными окружения (пример ниже).

Запустите миграции и суперпользователя:

```
python manage.py migrate
python manage.py createsuperuser
```
Запустите сервер:

```
python manage.py runserver
```

---

## Docker
Сборка и запуск
```
docker compose build
docker compose up
```
Запуск миграций и создание суперпользователя через Docker:
```
docker compose run web python manage.py migrate
docker compose run web python manage.py createsuperuser
```

---

## Переменные окружения (.env)
Создайте файл .env в корне проекта со следующим содержимым:

```
DEBUG=True
SECRET_KEY=your-secret-key
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
```

---

## Django Admin
Админка Django доступна по адресу:

http://103.71.21.184:8000/admin/

Используйте логин/пароль: admin/admin.

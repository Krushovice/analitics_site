install:
	./build.sh

start:
	poetry run python -m gunicorn sales_analitics_site.asgi:application -k uvicorn.
workers.UvicornWorker

migrate:
	poetry run python manage.py migrate

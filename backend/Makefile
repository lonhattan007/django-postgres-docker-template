default: up

bootstrap:
	docker build .
	docker compose up -d --build --remove-orphans
	make db-migrate
	echo "Happy coding!!! :tada:"
	
up:
	docker compose up -d --remove-orphans

down:
	docker compose down

ps:
	docker compose ps

update-packages:
	rm requirements.txt
	pip freeze >> requirements.txt

db-migrate:
	docker compose exec web python3 manage.py makemigrations
	docker compose exec web python3 manage.py migrate

test:
	docker compose exec web python3 manage.py test

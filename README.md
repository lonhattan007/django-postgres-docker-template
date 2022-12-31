# README.md

This is a template for a server side API project using `Django Rest framework` + `PostgreSQL` + `Docker`. The project resembles a todo app.

## Set up

- Clone this project
	```
	git clone git@github.com:lonhattan007/django-postgres-docker-template.git
	cd django-postgres-docker-template.git
	```

- Creating a virtual environment (for development). Here I use venv, you can use other virtual environment tools if you want.
	```
	python -m venv venv
	```
- Install packages
	```
	pip install -r ./backend/requirements.txt
	```
- Build Docker container
	```
	cd backend
	docker build .
	```

- Run the server in daemon mode
	```
	docker compose up -d
	```
	or in verbose mode
	```
	docker compose up
	```

## Workflow

### Commit changes when Docker is running:

- Grab the container ID:
	```
	docker ps
	```
- Commit changes:
	```
	docker commit <container_id>
	```
- Note: next time you might have to build the containers again:
	```
	docker compose up --build
	```

### Execute Django tasks with Docker Compose:
- We can use the Django CLI with Docker Compose while Docker is running
	```
	docker compose exec web python manage.py <command>
	```

- For example:
	```
	docker compose exec web python manage.py createsuperuser
	docker compose exec web python manage.py makemigrations
	docker compose exec web python manage.py createsuperuser
	docker compose exec web python manage.py test
	```

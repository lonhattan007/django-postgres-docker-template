# README.md

This is a template for a server side API project using `Django Rest framework` + `PostgreSQL` + `Docker`. The project resembles a todo app.

## Set up

- Clone this project:
	```
	git clone git@github.com:lonhattan007/django-postgres-docker-template.git
	cd django-postgres-docker-template.git
	```

- Create a virtual environment (for development). Here I use `venv`, you can use other virtual environment tools:
	```
	python -m venv venv
	. venv/bin/activate
	```
- Install packages:
	```
	pip install -r ./backend/requirements.txt
	```
- Build Docker container:
	```
	cd backend
	docker build .
	```

- Run the server in daemon mode:
	```
	docker compose up -d
	```
	or in verbose mode:
	```
	docker compose up
	```

## Workflow

### Virtual environment and package management
The following commands are run from the project `backend` directory, not the app `backend/backend`.

- During development, we need to activate the virtual environment and add its packages to the PYTHONPATH environment variable. The following commands work with `venv`:
  ```
  . venv/bin/activate
  export PYTHONPATH=$(pwd)/venv/lib/pythrunningon3.8/site-packages
  ``` 

- When we need to add or update changes to the packages, we also need to update the `backed/requirements.txt` file:
  ```
  rm backend/requirements.txt
  pip freeze >> requirements.txt
  ```
- When we don't need to use the virtual environment anymore, we can deactivate it from within the project:
  ```
  deactivate
  ```

### Commit changes when Docker is running:
The following commands are run from within the app `backend/backend` directory.

- Grab the container ID:
	```
	docker ps
	```
- Commit changes:
	```
	docker commit <container_id>
	```
- Note: next time we might have to build the containers again:
	```
	docker compose up --build
	```

### Execute Django tasks with Docker Compose:
The following commands are run from within the app `backend/backend` directory.

- We can use the Django CLI with Docker Compose while Docker is running:
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

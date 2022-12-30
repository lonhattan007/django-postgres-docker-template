This is a template for a Django Rest framework + PostgreSQL + Docker project.

Steps for setting up:

- Creating a virtual environment (for development)
	```
	python -m venv venv
	```
- Install packages
	```
	pip install -r ./budget_tracker_backend/requirements.txt
	```
- Build Docker containers
	```
	docker compose up -d --build
	```

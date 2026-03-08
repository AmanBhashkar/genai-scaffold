# Makefile for {{ project_name }}

.PHONY: dev build run shell migrate test

dev: ## Run the development server with hot-reloading
	docker compose -f docker-compose.dev.yml up --build

build: ## Build the production Docker image
	docker build -t {{ project_name }}:latest .

run: ## Run the production Docker container
	docker run -p 8000:8000 {{ project_name }}:latest

shell: ## Access the shell of the running app container
	docker compose exec app /bin/bash

migrate: ## Run database migrations
{% if database == 'postgres' %}
	docker compose exec app alembic upgrade head
{% else %}
	@echo "No migrations needed for MongoDB"
{% endif %}

test: ## Run the tests
	docker compose exec app uv run pytest

help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

MANAGE := poetry run python manage.py

.PHONY: test
test:
	@poetry run pytest

.PHONY: setup
setup: db-clean install migrate

.PHONY: install
install:
	@poetry install

.PHONY: db-clean
db-clean:
	@rm db.sqlite3 || true

.PHONY: migrate
migrate:
	@$(MANAGE) makemigrations && $(MANAGE) migrate

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

.PHONY: lint
lint:
	@poetry run flake8 task_manager

.PHONY: run
run:
	$(MANAGE) runserver

run-g:
	poetry run gunicorn task_manager.wsgi
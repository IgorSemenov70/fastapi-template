.ONESHELL:
.PHONY: install lint tests migrate run

define setup_env
    $(eval ENV_FILE := $(1))
    @echo " - setup env $(ENV_FILE)"
    $(eval include $(1))
    $(eval export)
endef

install:
	@echo "---- 👷 Installing build dependencies ----"
	poetry install
	poetry run pre-commit install --install-hooks

lint:
	rm -rf .mypy_cache .ruff_cache
	#poetry run ruff --fix src tests
	poetry run black src tests
	#poetry run mypy src tests
	poetry run isort src tests --profile black

tests:
	rm -rf .pytest_cache
	@echo ---- ⏳ Running tests ----
	@(poetry run pytest -v --cov --cov-report term && echo "---- ✅ Tests passed ----" && exit 0 || echo "---- ❌ Tests failed ----" && exit 1)

migrate:
	docker compose --profile migration up --build

run:
	poetry run uvicorn --factory src.presentation.api.main:create_app --host 0.0.0.0 --port 8000
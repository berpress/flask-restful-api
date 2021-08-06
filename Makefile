lint:
	@pre-commit run --all-files

start:
	python app.py

test:
	@pytest tests/api -q

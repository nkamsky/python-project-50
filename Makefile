install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

check:
	poetry run flake8 gendiff
	poetry run pytest
	
test-coverage:
	poetry run pytest --cov=gendiff --cov-report=term-missing

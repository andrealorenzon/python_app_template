# python app template

1. change app name in `pyproject.toml`
2. run `poetry install` 

Type annotation enforced.

Scripts:

* `poetry run lint` -> flake8 + black + mypy + vulture
* `poetry run format` -> check formatting with black
* `poetry run reformat` -> fix formatting errors with black
* `poetry run test` -> run all tests with pytest
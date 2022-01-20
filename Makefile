# Guard against running Make commands outside a virtualenv or conda env
venv:
ifndef VIRTUAL_ENV
ifndef CONDA_PREFIX
$(error VIRTUAL / CONDA ENV is not set - please activate environment)
endif
endif

clean: venv
	@echo "Removing build artifacts / temp files"
	find . -name "*.pyc" -delete

test: venv
	pip install -U pytest --force-reinstall
	pip install pytest-cov
	pytest --cov-report term-missing --cov-report html --cov-branch --cov=glogging tests

deps: venv
	pip install -U pip setuptools
	pip install -e .

all: venv deps clean

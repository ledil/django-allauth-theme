.PHONY: clean build deploy install publish

# Project settings
PROJECT = django-allauth-theme

# Virtual environment settings
ENV ?= venv
REPOSITORY ?= pypi

requirements = -r requirements-dev.txt

all: install build

clean:
	@echo "Cleaning..."
	@rm -rf ./build ./*egg* ./.coverage ./dist

build: clean
	@echo "Building..."
	@pip install -U setuptools
	@python3 setup.py sdist

publish: build
	@echo "Publishing to $(REPOSITORY)..."
	@twine upload -r $(REPOSITORY) dist/*

register:
	@echo "Registering package on $(REPOSITORY)..."
	@$(ENV)/bin/twine register -r $(REPOSITORY)

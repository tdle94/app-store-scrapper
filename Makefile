build:
	python setup.py sdist bdist_wheel

clean:
	python setup.py clean --all
	rm -rf dist

lint:
	flake8 app-store-scrapper tests

fmt:
	black app-store-scrapper tests

test:
	python -m unittest discover

test-all:
	detox

test-debug:
	python -m unittest discover -v

.PHONY: build
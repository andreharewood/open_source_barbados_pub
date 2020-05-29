# Barbados

Barbadian energy system datapackage following the datapackage format described in [oemof-tabular](https://oemof-tabular.readthedocs.io/en/latest/usage.html#datapackage).

# Installation

Create a new virtual environment.

	mkvirtualenv Barbados

Install the requirements. We need a pip version, that supports dependency links.

	pip install pip==18.1
	pip install --process-dependency-links -r requirements.txt

To run the model.

	python compute.py

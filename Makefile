install:
	python3 -m venv venv
	virtualenv venv
	. venv/bin/activate
	pip install -r requirements.txt

test:
	. venv/bin/activate
	pytest --cov=settings_manager tests

ui:
	. venv/bin/activate
	python -m settings_manager.ui

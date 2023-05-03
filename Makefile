install:
	pip install virtualenv
	virtualenv venv
	. venv/bin/activate
	pip install -r requirements.txt

test:
	. venv/bin/activate
	pytest --cov=settings_manager tests --cov-report=html

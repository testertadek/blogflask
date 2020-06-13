deps:
	pip install -r requirements.txt;

lint:
	flake8 flaskblog test

run:
	PYTHONPATH=. FLASK_APP=flaskblog flask run

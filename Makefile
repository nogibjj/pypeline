install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black src/*.py 

lint:
	pylint --disable=R, src/*.py

refactor: format lint
		
all: install lint test format deploy
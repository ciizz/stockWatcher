run:
	flask --app app run

unittests:
	python3 -m unittest discover -s tests -p "test/*.py"

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf __pycache__


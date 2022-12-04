run:
	flask --app app run

unittests:
	python3 -m unittest discover -s test -p '*_tests.py' -v

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf __pycache__ model/__pycache__ test/__pycache__


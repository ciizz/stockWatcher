run:
	flask --app app run

unittests:
	python3 -m unittest discover -s test/unit -p '*_tests.py' -v

integrationtests:
	python3 -m unittest discover -s test/integration -p '*_tests.py' -v

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf __pycache__ model/__pycache__ test/__pycache__ test/unit/__pycache__ test/integration/__pycache__


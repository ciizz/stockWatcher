all: run setup test clean
.phony: all

setup:requirements.txt 
	pip install -r requirements.txt

run:
	flask --app app run

test:   
	python3 -m unittest discover -s test -p "test/*.py"

clean:  
	rm -rf __pycache__


all: run setup test clean
.phony: all

run:
    flask --app app run

setup: requirements.txt
    pip install -r requirements.txt

test:
    python3 -m unittest discover -s test -p "test/*.py"

clean: 
    rm -rf __pycache__


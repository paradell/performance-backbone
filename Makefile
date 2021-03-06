VENV_PATH  := .performance_venv

all: clean_virtualenv create_virtualenv activate_virtualenv install_requirements

clean_virtualenv:
	rm -rf $(VENV_PATH)

create_virtualenv:
	virtualenv -p /usr/bin/python2.7 $(VENV_PATH)

activate_virtualenv:
	@echo "run manually: 'source $(VENV_PATH)/bin/activate'"
	@echo "And then run 'make install_requirements'"
	exit 1

install_requirements:
	pip install -r requirements.txt

run_locust_test:
	locust --no-web --clients=100 --hatch-rate=10 --num-request=5000 --locustfile=locust/locust_test.py

run_multi_mechanize_test:
	multimech-run multimech

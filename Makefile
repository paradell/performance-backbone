VENV_PATH  := .smart_notif_venv

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


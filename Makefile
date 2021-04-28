SHELL:=/bin/bash

.PHONY: venv help run clean

PYTHON=python3

.DEFAULT_GOAL=run

ACT=source venv/bin/activate

venv:
	@echo "----------------VENV----------------"; \
	${PYTHON} -m venv venv; \
	pip install -r requirements.txt;


run:
	@echo "---------------RUN------------------"; \
	declare -x DISPLAY=":0"; \
	export DISPLAY; \
	${ACT}; \
	${PYTHON} app.py;


clean:
	@rm -r venv
.PHONY: install create-env install-env help

ENV-DIR = ~/env-noema
ENV = @. $(ENV-DIR)/bin/activate
REQ = requirements.txt

help:
	@echo develop - create develop env for project;\
	echo install - install project on system

develop: create-env install-env-deps
	

create-env:
	@if [ ! -d $(ENV-DIR) ]; then\
	    echo Env not exists;\
	    echo Create env...;\
	    virtualenv ~/env-noema;\
	    echo Done;\
	else\
	    echo Env exists;\
	fi\

install-env-deps:
	$(ENV) && pip install -r $(REQ) --upgrade

install:
	@echo Not implemented yet
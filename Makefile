.PHONY: install create-env install-env help

BASE = noema
ENV-DIR = ~/env-$(BASE)
ENV = . $(ENV-DIR)/bin/activate
REQ = requirements.txt

SQLUSER = root
SQLPASS = root

help:
	@echo develop - create develop env for project;\
	echo install - install project on system

develop: install-env-deps create-db
	

create-env:
	@if [ ! -d $(ENV-DIR) ]; then\
	    echo Env not exists;\
	    echo Create env...;\
	    virtualenv $(ENV-DIR);\
	    echo Done;\
	else\
	    echo Env exists;\
	fi\

install-env-deps: create-env
	@echo Check requirements...;\
	$(ENV) && pip install -r $(REQ) --upgrade

create-db:
	@mysql -u $(SQLUSER) -p$(SQLPASS) -e 'CREATE DATABASE IF NOT EXISTS $(BASE)'

install:
	@echo Not implemented yet

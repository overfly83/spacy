@echo off
set http_proxy=http://proxy.van.sap.corp:8080
set https_proxy=http://proxy.van.sap.corp:8080
IF NOT EXIST env (
	echo "Install virtual environment."
	pip3 install virtualenv
	py -m virtualenv env
) else (
	echo "Skip installing virtualenv."
)
call env\Scripts\python setup.py install
call env\Scripts\python -m spacy download en_core_web_sm

@echo off
IF NOT EXIST env (
	echo "Install virtual environment."
	pip3 install virtualenv
	py -m virtualenv env
) else (
	echo "Skip installing virtualenv."
)
call env\Scripts\python setup.py install
call env\Scripts\python -m spacy download en_core_web_sm

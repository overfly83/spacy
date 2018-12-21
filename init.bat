@echo off
IF NOT EXIST env (
	echo "Install virtual environment."
	pip3 install virtualenv
	py -m virtualenv env
	venv\Scripts\activate
) else (
	echo "Skip installing virtualenv."
)
python setup.py install
python -m spacy download en_core_web_sm

#!/usr/bin/env bash

if [ ! -d ".env" ]; then
	python3 -m venv .env
	source .env/bin/activate
	pip install -r requirements.txt
else
	source .env/bin/activate
fi

python main.py



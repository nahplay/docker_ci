#!/bin/bash

cd "home"
pip install -r requirements.txt
pylint main.py
python main.py
#!/bin/bash
source ~/.bashrc
python3 -m coverage run pytest tests/db_testing.py
python3 -m coverage report
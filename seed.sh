#!/bin/bash

pip3 install --upgrade pip && \
pip3 install -r requirements.txt

python3 ./seed/seed.py

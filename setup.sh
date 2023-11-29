#!/bin/bash

pip3 install --upgrade pip && \
pip3 install -r requirements.txt

python3 ./setup/1_describe_tables.py && \
python3 ./setup/2_ingest_chromadb.py

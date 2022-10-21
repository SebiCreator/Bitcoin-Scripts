#! /usr/bin/bash
#

ls -alt tests/*-test*.py

python3 tests/utils-test.py
python3 tests/transactions-test.py


#!/bin/bash
`python3 -m venv env`
source env/bin/activate
pip install -U psycopg2 xmltodict shapely
pip freeze -> requirements.txt

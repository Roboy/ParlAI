#!/usr/bin/env bash

python3 roboy_setup.py sdist bdist_wheel
twine upload dist/*
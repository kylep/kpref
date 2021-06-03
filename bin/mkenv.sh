#!/bin/bash
# Create the virtualenv
if [[ ! -d bin ]]; then
  cd ..
fi
virtualenv --python=python3 env/

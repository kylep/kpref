#!/bin/bash
hypercorn --debug --bind "0.0.0.0:80" kprefpyapi.main:app

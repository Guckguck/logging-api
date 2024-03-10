#!/bin/bash

# Umgebungsvariable LOG_LEVEL
# DEBUG, INFO, ERROR, FATAL
# Entferne Kommentare für den gewünschten Log-Level
export LOG_LEVEL=DEBUG
# export LOG_LEVEL=INFO
# export LOG_LEVEL=ERROR
# export LOG_LEVEL=FATAL

python3 main.py
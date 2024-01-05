#!/bin/bash

# Check if python3 is installed
if command -v python3 &>/dev/null; then
    python3 converter_guy.py
else
    echo "Python 3 is not installed. Please install it and try again."
fi


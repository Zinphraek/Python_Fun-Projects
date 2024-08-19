#!/usr/bin/env bash

# Activate the virtual environment
source Codes/python-fun-projects/pfpvenv/bin/activate

# Check if the virtual environment was activated successfully
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Virtual environment activated: $VIRTUAL_ENV"

    # Run the Python script
    python3 Codes/python-fun-projects/multiclip.py 'agree'
else
    echo "Failed to activate virtual environment."
    exit 1
fi
bash

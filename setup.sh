#!/bin/bash

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created."
else
    echo "📁 Virtual environment already exists."
fi

# Activate the environment
source venv/bin/activate

# Install dependencies
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "📦 Dependencies installed from requirements.txt."
else
    echo "⚠️ requirements.txt not found!"
fi

# Done
echo "✅ Environment is ready. To activate it later, run: source venv/bin/activate"

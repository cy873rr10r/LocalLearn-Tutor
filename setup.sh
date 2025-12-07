#!/bin/bash

# LocalLearn Setup Script
echo "🌍 LocalLearn - Science in Your Language & Style"
echo "================================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
echo "Python version: $python_version"

if (( $(echo "$python_version < 3.8" | bc -l) )); then
    echo "❌ Error: Python 3.8+ required"
    exit 1
fi

echo "✅ Python version OK"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Error installing dependencies"
    exit 1
fi

echo ""
echo "================================================"
echo "✅ Setup complete!"
echo ""
echo "To run the app:"
echo "  streamlit run main.py"
echo ""
echo "Then open: http://localhost:8501"
echo "================================================"

#!/bin/bash

echo "Running linting checks..."

echo "1. Running flake8..."
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

echo "2. Checking code formatting with black..."
black --check --diff .

echo "3. Checking import sorting with isort..."
isort --check-only --diff .

echo "4. Checking docstrings with pydocstyle..."
pydocstyle --convention=google src/

echo "5. Type checking with mypy..."
mypy src/ --ignore-missing-imports

echo "6. Checking for missing docstrings in functions..."
python -c "
import ast
import os

def check_docstrings(filepath):
    with open(filepath, 'r') as f:
        try:
            tree = ast.parse(f.read())
        except SyntaxError:
            return
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if not ast.get_docstring(node):
                    print(f'Missing docstring in function {node.name} at {filepath}:{node.lineno}')
                    exit(1)

for root, dirs, files in os.walk('src'):
    for file in files:
        if file.endswith('.py'):
            check_docstrings(os.path.join(root, file))
"

echo "All linting checks completed!"

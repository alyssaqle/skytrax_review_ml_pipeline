## Description
Brief description of the changes made in this PR.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement
- [ ] Other (please describe):

## Testing
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] I have tested this change locally
- [ ] All CI checks pass

## Code Quality
- [ ] My code follows the project's coding standards
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added docstrings to all new functions and classes

## Code Formatting
Before submitting this PR, please ensure your code is properly formatted:

### Quick Format Commands
```bash
# Format all Python files
black . && isort .

# Check what will be changed (dry run)
black --check --diff .
isort --check-only --diff .

# Run all linting checks locally
./lint_check.sh
```

### Individual Tool Commands
```bash
# Format code with black
black src/

# Sort imports with isort
isort src/

# Check linting with flake8
flake8 src/

# Check docstrings with pydocstyle
pydocstyle --convention=google src/

# Type check with mypy
mypy src/ --ignore-missing-imports
```

## Documentation
- [ ] I have updated the README.md if necessary
- [ ] I have updated any relevant documentation
- [ ] I have added comments explaining complex code sections

## Checklist
- [ ] My code is properly formatted (black, isort)
- [ ] My code passes all linting checks (flake8, pydocstyle)
- [ ] My code has proper type hints where applicable
- [ ] All functions have docstrings following Google style
- [ ] No hardcoded values or magic numbers
- [ ] Error handling is implemented where appropriate

## Additional Notes
Any additional information, context, or screenshots that would help reviewers understand the changes.

## Related Issues
Fixes #(issue number)
Related to #(issue number)

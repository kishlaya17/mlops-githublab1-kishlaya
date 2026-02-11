# mlops-githublab1-kishlaya

This lab demonstrates how to use GitHub Actions to automate testing for a simple Python calculator module.

## What I Implemented

- Basic calculator functions:
  - add
  - subtract
  - multiply
  - divide (with zero handling)
- A custom `combined_operation` function:
  
  (x + y) + (x - y) + (x * y)

- Automated testing using:
  - Pytest
  - Unittest
- CI workflows using GitHub Actions
- flake8 linting for code quality

## Project Structure

- `src/` → calculator implementation  
- `test/` → pytest and unittest test files  
- `.github/workflows/` → CI workflow files  

## Running Locally

Install dependencies:
pip install -r requirements.txt

Run pytest:


Run unittest:

python -m unittest discover -s test

## CI

GitHub Actions runs automatically on push and pull request.  



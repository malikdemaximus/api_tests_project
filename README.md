# API Tests Project

## Description
Simple API automation tests using Python, Requests, and Pytest for the public API: https://reqres.in/

## Project Structure
api_tests_project/
│
├── tests/
│   ├── test_users.py
│   └── test_products.py
│
├── data/
│   └── test_data.json
│
├── utils/
│   └── api_helpers.py
│
├── conftest.py
├── requirements.txt
├── pytest.ini
├── Jenkinsfile
├── README.md
└── .gitignore

## How to run

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # for Linux/Mac
   venv\Scripts\activate   # for Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests:
   ```bash
   pytest
   ```

4. Generate HTML report:
   ```bash
   pytest --html=report.html
   ```

## CI/CD (Jenkins)
Project includes `Jenkinsfile` for running tests via Jenkins with HTML report generation.

### Jenkinsfile contains:
- Clone the GitHub repo
- Install dependencies
- Run tests
- Archive HTML report


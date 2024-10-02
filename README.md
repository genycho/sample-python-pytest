# pytest exercise project

## This is an sample application to exercise pytest

(1) basic of pytest and code test coverage(Line/Branch) 

(2) using Mock(pytest-mock) to unit-test 

(3) FastAPI application and its integration-testing(HTTP API Test) using test_client that FastAPI provides

All contents are copyright by si.choung(genycho) 


## Running this exercise locally
```
	execute the below pytest command in IDE terminal venv

	python -m pytest -v ./tests --junitxml="./TEST_RESULT.xml" --html="./test_result.html" --self-contained-html --cov-report html --cov-branch --cov=src ./temp_coverage

```

You can then access this project source here: [](http://localhost:8080/)


## Working with this exercise in your IDE

### Prerequisites
install the following libraries:

* python3 -m venv venv # 파이썬 가상환경 만들기

* source ./venv/bin/activate # 가상환경 활성화

* pip install pytest

* pip install pytest-cov

* pip install pytest-mock

* pip install pytest-html

* pip install fastapi==0.74.1 # fastapi 설치

* pip install "uvicorn[standard]" # uvicorn 설치

* pip install pytest-asyncio

* uvicorn src.coffee_restservice.fastapi_server:app --reload

 http://127.0.0.1:8000
 http://127.0.0.1:8000/docs
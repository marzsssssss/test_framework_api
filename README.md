## Test API Framework


## Useful commands (Example Accounts)

Start Smoke Tests
```sh
pytest tests/accounts/test_accounts_api.py
```

Start Flow Tests
```sh
pytest tests/accounts/test_accounts_flow.py
```

Start Negative Tests
```sh
pytest tests/accounts/test_accounts_negative.py
```
Start Allure Report
```sh
pytest tests/accounts/test_accounts_negative.py --alluredir=reports/allure
```

Up Allure Server
```sh
allure serve reports/allure   
```

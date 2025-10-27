import pytest
import allure
from faker import Faker 

from config.base_test import BaseTest
from core.headers import Headers

@allure.feature('Test Services - Accounts - Negative')
class TestAccountsNegative(BaseTest):

    fake = Faker()

    @allure.title('Negative Tests Accounts Headers')
    @pytest.mark.parametrize(
        ('headers ,expected_status'), [
            (Headers.invalid_token, 401),
            (Headers.missing_token, 401)
        ]
    )
    def test_accounts_headers(self, headers, expected_status, get_currency_id, get_ewallet_id):
        self.accounts_api_negative.logger.info(f'Test launch Negative Headers  - GET /accounts/total-amount/, headers -  {headers} - expected status - {expected_status}')
        self.accounts_api_negative.total_amount_negative(headers, expected_status,get_currency_id) 
        self.accounts_api_negative.logger.info(f'Test launch Negative Headers  - POST /accounts/ewallets/, headers -  {headers} - expected status - {expected_status}')
        self.accounts_api_negative.create_entity_ewallet(headers, expected_status, get_currency_id) 
        self.accounts_api_negative.logger.info(f'Test launch Negative Headers  - GET  /accounts/ewallets/, headers -  {headers} - expected status - {expected_status}')
        self.accounts_api_negative.get_accounts_ewallet_negativ(headers,expected_status)
        self.accounts_api_negative.logger.info(f'Test launch Negative Headers  - GET /accounts/ewallets/currencies/, headers -  {headers} - expected status - {expected_status}')
        self.accounts_api_negative.get_ewallet_currencies(headers, expected_status)
        self.accounts_api_negative.logger.info(f'Test launch Negative Headers  - GET /accounts/ewallets/{get_ewallet_id}/, headers -  {headers} - expected status - {expected_status}')
        self.accounts_api_negative.get_entity_ewallets(headers,expected_status, get_ewallet_id)

    @allure.title('Negative Tests Accounts UUID')
    @pytest.mark.parametrize(
        ('uuid ,expected_status_create, expected_status_get'), [
            ('invalid uuid',422, 404),
            ('12345', 422, 404),
            (fake.uuid4(), 400, 404),
        ]
    )
    def test_accounts_uuid(self, uuid, expected_status_create, expected_status_get, headers = Headers.basic):
        self.accounts_api_negative.logger.info(f'Test launch Negative UUID  - POST /accounts/ewallets/, uuid  -  {uuid} - expected status - {expected_status_create}')
        self.accounts_api_negative.create_entity_ewallet(headers, expected_status_create, uuid)
        self.accounts_api_negative.logger.info(f'Test launch Negative UUID  - GET /accounts/total-amount/{uuid}, uuid  -  {uuid} - expected status - {expected_status_get}')
        self.accounts_api_negative.total_amount_negative(headers, expected_status_get,uuid)
        self.accounts_api_negative.logger.info(f'Test launch Negative UUID  - GET /accounts/ewallets/{uuid}/, uuid  -  {uuid} - expected status - {expected_status_get}')
        self.accounts_api_negative.get_entity_ewallets(headers,expected_status_get, uuid)

    
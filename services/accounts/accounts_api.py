import allure

from utils.helper import Helper 
from services.accounts.endpoints import Endpoints
from core.headers import Headers
from payloads.accounts_payloads import Payloads
from models.accounts_model import (
    TotalAmountModel,
    CreateEntityEwalletModel,
    GetAccountAmountModel,
    GetEwalletCurrenciesModel,
    GetEwalletsEntityModel,
)

class AccountsAPI(Helper):

    def __init__(self, client):
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.payloads = Payloads()
        self.client = client

    @allure.step('Total Amount User')
    async def total_amount(self, currency_id):
        response = await self.client.get(
            url = self.endpoints.total_amount(currency_id),
            headers=self.headers.basic,
        )
        self.assert_response(response)
        model = TotalAmountModel(**response.json())
        self.attach_response_to_allure(response)
        return model
        
    @allure.step('Get Accounts Ewallet')
    async def get_accounts_ewallet(self):
        response = await self.client.get(
            url = self.endpoints.get_accounts_ewallet,
            headers=self.headers.basic
        )
        self.assert_response(response)
        model = GetAccountAmountModel(**response.json())
        self.attach_response_to_allure(response)
        return model
    
    @allure.step('Get Ewallet Currencies')
    async def get_ewallet_currencies(self):
        response = await self.client.get(
            url = self.endpoints.get_ewallet_currencies,
            headers=self.headers.basic
        )
        self.assert_response(response)
        response_json = response.json()
        model = GetEwalletCurrenciesModel(data = response_json)
        self.attach_response_to_allure(response)
        return model

    @allure.step('Get Entity Ewallets')
    async def get_entity_ewallets(self,currency_id):
        response = await self.client.get(
            url = self.endpoints.get_entity_ewallets(currency_id),
            headers=self.headers.basic
        )
        self.assert_response(response)
        model = GetEwalletsEntityModel(**response.json())
        self.attach_response_to_allure(response)
        return model
    
    @allure.step('Create Entity Ewallet')
    async def create_entity_ewallet(self, currency_id):
        response = await self.client.post(
            url=self.endpoints.create_entity_ewallet,
            headers = self.headers.basic,
            json = self.payloads.entity_ewallet(currency_id)
        )
        self.assert_response(response)
        model = CreateEntityEwalletModel(**response.json())
        self.attach_response_to_allure(response)
        return model
    
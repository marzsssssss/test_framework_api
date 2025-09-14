import allure
import pytest

from utils.helper import Helper
from services.admin_entities.endpoints import Endpoints


class AdminEntitiesNegative(Helper):

    def __init__(self, client):
        super().__init__()
        self.endpoints = Endpoints()
        self.client = client
        
    @allure.step('GET - /admin/entities/accounts/ Negative')
    async def get_entities_accounts(self, name, headers, expected_status):
        response = await self.client.get(
            url = self.endpoints.get_entities_accounts_list(name),
            headers=headers
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response_to_allure(response)

    @allure.step('POST- /admin/entities/accounts/adjust-balance Negative')
    async def post_entities_accounts_adjust(self, json, headers, expected_status):
        response = await self.client.post(
            url = self.endpoints.post_entities_accouts_adjust_balance,
            headers = headers,
            json = json
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response_to_allure(response)
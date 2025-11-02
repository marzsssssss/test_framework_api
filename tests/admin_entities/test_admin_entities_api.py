import allure
import os
import pytest

@allure.epic('Test Services - Admin Entities')
@pytest.mark.adminentities
class TestAdminEntities():

    @pytest.mark.asyncio
    @allure.title('Test  GET /admin/entities/accounts/un_name')
    async def test_get_entities_account_list(self, base):
        base.logger.get().info(f'Test launch - GET /admin/entities/accounts/un_name')
        await base.admin_entities_api.get_entities_accounts_list(os.getenv('UN_NAME'))

    @pytest.mark.asyncio
    @allure.title('Test POST /admin/entities/accounts/adjust-balance/')
    async def test_post_accounts_adjust_balance(self,get_ewallet_id, base):
        base.logger.get().info('Test launch - POST /admin/entities/accounts/adjust-balance/')
        await base.admin_entities_api.post_entities_accounts_adjust_balance(get_ewallet_id)
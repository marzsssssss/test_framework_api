import allure 

from utils.helper import Helper
from core.headers import Headers
from services.admin_invoices.endpoints import Endpoints
from models.admin_invoices.invoices_adjustment_invoices_model import InvoicesAdjustmentInvoicesModel
from models.admin_invoices.invoices_adjustment_model import InvoicesAdjustmentModel
from models.admin_invoices.invoices_withdrawal_invoices_model import InvoicesWithdrawalInvoicesModel
from models.admin_invoices.invoices_withdrawal_model import InvoicesWithdrawalModel



class AdminInvoicesAPI(Helper):

    def __init__(self, client):
        super().__init__()
        self.headers = Headers()
        self.endpoints = Endpoints()
        self.client = client

    @allure.step('GET /admin/invoices/withdrawal/')
    async def get_invoices_withdrawal(self):
        response = await self.client.get(
            url = self.endpoints.get_invoices_withdrawal,
            headers = self.headers.basic
        )
        self.assert_response(response)
        model = InvoicesWithdrawalModel(**response.json())
        self.attach_response_to_allure(response)
        return model

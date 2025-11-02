from services.accounts.accounts_api import AccountsAPI
from services.accounts.accounts_api_negative import AccountsNegativeAPI
from services.admin_entities.admin_entities_api import AdminEntitiesAPI
from services.admin_entities.admin_entities_api_negative import AdminEntitiesNegative
from services.admin_invoices.admin_invoices_api import AdminInvoicesAPI
from core.logger import Logger

class BaseTest:

    def __init__(self, client):
        self.logger = Logger('Base Test')
        self.accounts_api = AccountsAPI(client)
        self.accounts_api_negative = AccountsNegativeAPI(client)
        self.admin_entities_api = AdminEntitiesAPI(client)
        self.admin_entities_api_negative = AdminEntitiesNegative(client)
        self.admin_invoices_api = AdminInvoicesAPI(client)
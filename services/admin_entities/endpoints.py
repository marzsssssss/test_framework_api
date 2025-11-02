import os 

class Endpoints():
    
    get_entities_accounts_list = lambda self, unovay_name: f"{os.getenv('HOST')}/admin/entities/accounts/{unovay_name}/"

    post_entities_accounts_adjust_balance = f"{os.getenv('HOST')}/admin/entities/accounts/adjust-balance/"
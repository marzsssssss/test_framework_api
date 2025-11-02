import os 

class Endpoints:

    get_invoices_withdrawal = f"{os.getenv('HOST')}/admin/invoices/withdrawal/"

    get_invoices_withdrawal_invoice = lambda self, invoice_id: f"{os.getenv('HOST')}/admin/invoices/withdrawal/{invoice_id}/"

    post_invoices_complete = lambda self, invoice_id: f"{os.getenv('HOST')}/admin/invoices/withdrawal/{invoice_id}/complete/"

    post_invoices_cancel = lambda self, invoice_id: f"{os.getenv('HOST')}/admin/invoices/withdrawal/{invoice_id}/cancel/"

    get_invoices_adjustment = f"{os.getenv('HOST')}/admin/invoices/adjustment/"

    get_invoices_adjustment_invoice = lambda self, invoice_id: f"{os.getenv('HOST')}/admin/invoices/adjustment/{invoice_id}/"
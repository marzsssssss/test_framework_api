from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import List


class Meta(BaseModel):
    limit: int
    total: int
    current_page: int
    last_page: int


class User(BaseModel):
    id: UUID
    full_name: str
    unovay_name: str


class Currency(BaseModel):
    id: UUID
    code: str
    symbol: str
    name: str
    is_popular: bool
    is_used: bool
    priority: int
    file_meta_id: UUID
    flag: str


class Country(BaseModel):
    id: UUID
    name: str
    full_name: str
    code_2: str
    code_3: str
    phone_code: str
    file_meta_id: UUID
    flag: str


class DataItem(BaseModel):
    created_at: datetime
    updated_at: datetime
    updated_by_user: User
    id: UUID
    recipient_name: str
    recipient_account_number: str
    recipient_bank_swift: str
    recipient_bank_name: str
    recipient_address: str
    purpose: str
    payer_ewallet_id: UUID
    payer_entity_id: UUID
    payer_entity_type: str
    transfer_initiator: UUID
    payer_account_holder_name: str
    commission: str
    recipient_amount: str
    payer_amount: str
    payer_currency: Currency
    recipient_currency: Currency
    status: str
    recipient_country: Country
    invoice_type: str
    operation_type: str
    invoice_direction: str
    withdrawal_type: str


class InvoicesWithdrawalModel(BaseModel):
    meta: Meta
    data: List[DataItem]
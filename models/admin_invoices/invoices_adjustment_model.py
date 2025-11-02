from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List, Literal


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


class DataItem(BaseModel):
    created_at: datetime
    updated_at: datetime
    updated_by_user: User
    id: UUID

    recipient_name: str
    recipient_unovay_name: str
    recipient_entity_id: UUID
    recipient_ewallet_id: UUID
    recipient_entity_type: Literal["user", "business"]

    payer_ewallet_id: UUID
    payer_unovay_name: str
    payer_entity_id: UUID
    payer_account_holder_name: str
    payer_entity_type: Literal["user", "business"]

    recipient_amount: str
    payer_amount: str

    payer_currency: Currency
    recipient_currency: Currency

    status: Literal["SUCCESS", "FAILED", "PENDING"]
    invoice_type: Literal["INTERNAL", "EXTERNAL"]
    operation_type: Literal["TRANSFER", "PAYMENT", "WITHDRAWAL"]
    invoice_direction: Literal["SEND", "RECEIVE"]


class InvoicesAdjustmentModel(BaseModel):
    meta: Meta
    data: List[DataItem]
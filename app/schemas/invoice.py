from pydantic import BaseModel


class Invoice(BaseModel):
    invoice_link: str


class InvoiceBase(BaseModel):
    from_user_id: int
    currency: str
    total_amount: int
    invoice_payload: str


class InvoiceResponse(InvoiceBase):
    invoice_id: str

    class Config:
        from_attributes = True

from src.main.api.models.base_model import BaseModel


class UpdateDepositResponse(BaseModel):
    id : int
    balance : float
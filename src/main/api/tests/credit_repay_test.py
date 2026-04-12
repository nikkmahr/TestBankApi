import pytest
from sqlalchemy.orm import Session
from src.main.api.db.crud.credit_crud import CreditCrudDB as Credit
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.credit_repay_request import CreditRepayRequest

@pytest.mark.api

class TestCreditRepay:
    def test_user_credit_repay(self, db_session: Session, api_manager: ApiManager, user_with_credit):
        user, account, credit = user_with_credit
        request = CreditRepayRequest(creditId=credit.creditId, accountId=account.id, amount=credit.amount)
        response = api_manager.user_steps.credit_repay(user, request)

        assert response.creditId == credit.creditId
        credit_from_db = Credit.get_credit_by_id(db_session, credit.creditId)
        assert credit_from_db.balance == 0, 'После погашения кредита баланс в БД должен быть равен 0'



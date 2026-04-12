import pytest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.credit_request_request import CreditRequest
from sqlalchemy.orm import Session
from src.main.api.db.crud.credit_crud import CreditCrudDB as Credit

@pytest.mark.api
class TestCreditRequest:
    def test_credit_request(self, db_session: Session, api_manager: ApiManager, credit_user_account):
        user, account = credit_user_account
        request = CreditRequest(accountId=account.id, amount=5000, termMonths=12)
        response = api_manager.user_steps.credit_request(user, request)

        assert response.id == account.id
        credit_from_db = Credit.get_credit_by_id(db_session, response.creditId)
        assert credit_from_db is not None, 'Кредит должен существовать в БД'
        assert credit_from_db.account_id == account.id, 'ID кредита в БД не соответствует ожидаемому'




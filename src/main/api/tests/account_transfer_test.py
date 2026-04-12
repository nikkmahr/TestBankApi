import pytest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.account_transfer_request import AccountTransferRequest
from sqlalchemy.orm import Session
from src.main.api.db.crud.transactions_crud import TransactionCrudDB as Transaction

@pytest.mark.api

class TestAccountTransfer:
    def test_account_transfer(self, db_session: Session, api_manager: ApiManager, two_accounts_with_money):
        user1, account1, user2, account2 = two_accounts_with_money
        request = AccountTransferRequest(
            fromAccountId=account1.id,
            toAccountId=account2.id,
            amount=1000,
        )
        response = api_manager.user_steps.transfer_money(user1, request)
        assert response.fromAccountId == account1.id
        assert response.toAccountId == account2.id
        transaction_from_db = Transaction.get_transactions_by_from_account_id(db_session, response.fromAccountId)
        assert transaction_from_db.transaction_type is not None, 'Тип транзакции в БД не может быть пустым'
        assert transaction_from_db.transaction_type == "transfer", 'Тип транзакции в БД не соответствует ожидаемому'



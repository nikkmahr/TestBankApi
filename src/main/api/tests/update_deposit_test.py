import pytest
from sqlalchemy.orm import Session
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.update_deposit_request import UpdateDepositRequest
from src.main.api.db.crud.account_crud import AccountCrudDB as Account

@pytest.mark.api
class TestUpdateDeposit:
    def test_update_deposit_valid(self, db_session: Session, api_manager: ApiManager, user_account):
        user, account = user_account
        old_balance = account.balance
        request = UpdateDepositRequest(accountId=account.id, amount=1000)
        response = api_manager.user_steps.update_deposit(user, request)

        assert response.balance > old_balance
        deposit_from_db = Account.get_account_by_id(db_session, account.id)
        assert deposit_from_db is not None, 'Счет был не найден в БД'
        assert deposit_from_db.balance == old_balance + 1000, 'Баланс счета в БД не соответствует ожидаемому'



    @pytest.mark.parametrize(
        "amount",
        [ 999, 9001]
    )
    def test_update_deposit_invalid(self, db_session: Session, amount, api_manager: ApiManager, user_account):
        user, account = user_account
        old_balance = account.balance
        request = UpdateDepositRequest(accountId=account.id, amount= amount)
        response = api_manager.user_steps.update_deposit_invalid(user, request)
        assert "error" in response.text

        deposit_from_db = Account.get_account_by_id(db_session, account.id)
        assert deposit_from_db.balance == old_balance, 'Ошибка: баланс изменился при невалидном пополнении'

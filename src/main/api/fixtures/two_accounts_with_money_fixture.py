import pytest
from src.main.api.models.update_deposit_request import UpdateDepositRequest

@pytest.fixture
def two_accounts_with_money(api_manager, user_account_gen):
    user1, account1 = user_account_gen()
    user2, account2 = user_account_gen()

    account_money1 = api_manager.user_steps.update_deposit(user1, UpdateDepositRequest(accountId=account1.id, amount=2000))
    account_money2 = api_manager.user_steps.update_deposit(user2, UpdateDepositRequest(accountId=account2.id, amount=2000))

    return user1, account_money1, user2, account_money2
import pytest
from src.main.api.models.credit_request_request import CreditRequest

@pytest.fixture
def user_with_credit(api_manager, credit_user_account):
    user, account = credit_user_account
    credit_request = CreditRequest(
        accountId=account.id,
        amount=5000,
        termMonths=12
    )
    credit_response = api_manager.user_steps.credit_request(user, credit_request)
    return user, account, credit_response
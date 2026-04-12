import pytest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.fixture
def credit_user_account(api_manager):
    user = RandomModelGenerator.generate(CreateUserRequest)
    user.role = "ROLE_CREDIT_SECRET"
    api_manager.admin_steps.create_user(user)
    account = api_manager.user_steps.create_account(user)

    return user, account
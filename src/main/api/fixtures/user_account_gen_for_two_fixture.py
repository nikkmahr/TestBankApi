import pytest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.fixture
def user_account_gen(api_manager):
    def create():
        user = RandomModelGenerator.generate(CreateUserRequest)
        api_manager.admin_steps.create_user(user)
        account = api_manager.user_steps.create_account(user)
        return user, account
    return create
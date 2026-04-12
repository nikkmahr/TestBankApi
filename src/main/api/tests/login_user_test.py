import pytest
from src.main.api.models.login_user_request import LoginUserRequest

@pytest.mark.api
class TestLoginUser:
    def test_login_admin(self, api_manager):
        login_user_request = LoginUserRequest(username="admin", password="123456")
        response = api_manager.admin_steps.login_user(login_user_request)

        assert login_user_request.username == response.user.username
        assert response.user.role == "ROLE_ADMIN"

    def test_login_user(self, api_manager, created_user):
        response = api_manager.admin_steps.login_user(created_user)

        assert created_user.username == response.user.username
        assert response.user.role == "ROLE_USER"
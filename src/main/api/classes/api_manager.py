from typing import Any
from src.main.api.steps.admin_steps import AdminSteps
from src.main.api.steps.user_steps import UserSteps

# Этот класс отвечает за хранение всех степов
class ApiManager:
    def __init__(self, created_obj: list[Any]):     # Через него прокидываются все нужные данные для степов
        self.admin_steps = AdminSteps(created_obj)
        self.user_steps = UserSteps(created_obj)
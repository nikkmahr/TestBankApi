from src.main.api.models.account_transfer_request import AccountTransferRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_request_request import CreditRequest
from src.main.api.models.update_deposit_request import UpdateDepositRequest
from src.main.api.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.foundation.endpoint import Endpoint


class UserSteps(BaseSteps):
    def create_account(self, created_user: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=created_user.username, password=created_user.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    def update_deposit(self, created_user: CreateUserRequest, update_deposit_request: UpdateDepositRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=created_user.username, password=created_user.password),
            Endpoint.UPDATE_DEPOSIT,
            ResponseSpecs.request_ok()
        ).post(update_deposit_request)
        return response

    def update_deposit_invalid(self, created_user: CreateUserRequest, update_deposit_request: UpdateDepositRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=created_user.username, password=created_user.password),
            Endpoint.UPDATE_DEPOSIT,
            ResponseSpecs.request_bad()
        ).post(update_deposit_request)
        return response

    def transfer_money(self, created_user: CreateUserRequest , transfer_request: AccountTransferRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=created_user.username, password=created_user.password),
            Endpoint.TRANSFER_MONEY,
            ResponseSpecs.request_ok()
        ).post(transfer_request)
        return response

    def credit_request(self, created_user: CreateUserRequest, credit_request: CreditRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=created_user.username, password=created_user.password),
            Endpoint.CREDIT_GET,
            ResponseSpecs.request_created()
        ).post(credit_request)
        return response

    def credit_repay(self, created_user: CreateUserRequest, credit_repay: CreditRepayRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=created_user.username, password=created_user.password),
            Endpoint.CREDIT_REPAY,
            ResponseSpecs.request_ok()
        ).post(credit_repay)
        return response
from http import HTTPStatus
import requests
from src.main.api.models.update_deposit_response import UpdateDepositResponse
from src.main.api.models.update_deposit_request import UpdateDepositRequest
from src.main.api.requests.requester import Requester


class UpdateDepositRequester(Requester):
    def post(self, update_deposit_request: UpdateDepositRequest):
        url = f"{self.base_url}/account/deposit"
        response = requests.post(
            url=url,
            json=update_deposit_request.model_dump(),
            headers=self.headers
        )

        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return UpdateDepositResponse(**response.json())
        return response
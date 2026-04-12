from http import HTTPStatus
import requests
from src.main.api.models.credit_request_request import CreditRequest
from src.main.api.models.credit_request_response import CreditRequestResponse
from src.main.api.requests.requester import Requester


class CreditRequestRequester(Requester):
    def post(self, credit_request_request: CreditRequest):
        url = f"{self.base_url}/credit/request"
        response = requests.post(
            url=url,
            json = credit_request_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        if response.status_code == HTTPStatus.CREATED:
            return CreditRequestResponse(**response.json())
        return response


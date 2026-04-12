import requests
from src.main.api.models.account_transfer_request import AccountTransferRequest
from src.main.api.models.account_transfer_response import AccountTransferResponse
from src.main.api.requests.requester import Requester


class AccountTransferRequester(Requester):
    def post(self, account_transfer_request: AccountTransferRequest):
        url = f"{self.base_url}/account/transfer"
        response = requests.post(
            url=url,
            json=account_transfer_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        return AccountTransferResponse(**response.json())
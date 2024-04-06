"""This is a module.

Here can be some info about the module.

Here we have the RequestMonitor and import the messenger.
"""

import example_2

from typing import List
import logging


class RequestMonitor:
    """This is another docstring."""

    LIST_OF_ENDPOINTS: List[str] = ["endpoint_1", 'endpoint2_2']
    EXPECTED_RESPONSE_CODE: str = "200"
    # CATEGORY_PER_ENDPOINT: Dict[str, str] = {
    #     "endpoint_1": "config squad"
    # }
    # logging.basicConfig(
    #     format=""
    # )
    LOGGER: logging.Logger = logging.getLogger()
    MESSENGER: example_2.Messenger = example_2.Messenger()

    def __init__(self, name: str = "default_name"):
        self.name = name

    def send_request(self, endpoint: str) -> str:
        """This is a docstring

        Args:
            endpoint (str): _description_

        Returns:
            str: _description_
        """

    def check_response(self, response_code: str):
        pass

    def categorize_response(self, endpoint: str):
        pass

    def send_message(self):
        self.LOGGER.info("Logger: This is an info!")
        self.MESSENGER.send_message()
        print(self.name)


RequestMonitor.EXPECTED_RESPONSE_CODE = "something_else"
monitor = RequestMonitor()
monitor.send_message()

import time

import validators
import requests
from bs4 import BeautifulSoup
import re

from logger import Logger
from metric import Metric
from producer import Producer


class Checker:
    def __init__(self,
                 target_url: str,
                 regex: str,
                 producer: Producer,
                 logger: Logger):
        validators.url(target_url)

        self.regex = re.compile(regex, re.IGNORECASE | re.MULTILINE | re.DOTALL)

        self.target_url = target_url
        self.producer = producer
        self.logger = logger.get_logger("Checker")

    def check(self):
        self.logger.debug("Checking...")

        start = time.process_time()
        response = requests.get(self.target_url)
        request_time = (time.process_time() - start) * 1000

        self.logger.debug(f"Time: {request_time} ms")

        self.logger.debug(f"Status code: {response.status_code}")

        soup = BeautifulSoup(response.text, 'html.parser')
        occurrences = self.regex.findall(soup.text)

        found = len(occurrences) > 0

        self.logger.debug(f"Found: {found}")

        # self.producer.produce(metrics)

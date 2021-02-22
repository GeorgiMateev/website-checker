from typing import List

from metric import Metric
from logger import Logger


class Producer:
    def __init__(self, logger: Logger):
        self.logger = logger.get_logger("Producer")

    def produce(self, metrics: List[Metric]):
        self.logger.debug(f"Metrics: {str(metrics)}")
        pass

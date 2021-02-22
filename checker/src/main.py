import os

from time import sleep

from checker import Checker
from logger import Logger
from producer import Producer

if __name__ == '__main__':
    log_level = os.getenv("LOG_LEVEL", "INFO")
    logger = Logger(log_level)
    main_logger = logger.get_logger("main")

    interval_ms = int(os.getenv("INTERVAL_MS", 1000))

    main_logger.info(f"Checks will be performed each {interval_ms} ms."
                     f"provide INTERVAL_MS env variable to change that.")

    target_url = os.getenv("TARGET_URL")
    if not target_url:
        raise Exception("Please provide target url in TARGET_URL env var.")
    main_logger.info(f"Target: {target_url}")

    regex = os.getenv("REGEX")
    main_logger.info(f"Regex to search: {regex}")

    producer = Producer(logger)
    checker = Checker(target_url, regex, producer, logger)
    while True:
        checker.check()
        sleep(interval_ms / 1000)

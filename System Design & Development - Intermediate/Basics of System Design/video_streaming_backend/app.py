from consumer import *
import logging

logging.basicConfig(
    filename="logging_file.log",
    format="%(levelname)s - %(asctime)s - %(message)s",
    filemode="w",
)
logger = logging.getLogger("Streaming_data")
logger.setLevel(logging.CRITICAL)

class App:
    def __init__(self) -> None:
        logger.info("Application started")
        self.consumer = ConsumerClass()

    def run(self):
        self.consumer.run()

App().run()

import logging

from aiokafka import AIOKafkaProducer

from libs import config_loader
from libs.logger_colorer import colored_stream


config = config_loader.Config()
logging.basicConfig(
    level=logging.getLevelName(config.get(config_loader.LOGGING_LEVEL)),
    format=config.get(config_loader.LOGGING_FORMAT),
    handlers=[
        colored_stream,
    ],
)
logger = logging.getLogger(__name__)


class KafkaClient:
    def __init__(self, config: config_loader.Config):
        self.config = config
        self.producer = None

    async def producer_start(self):
        logger.info("Starting kafka producer")
        producer = AIOKafkaProducer(
            bootstrap_servers=self.config.get(config_loader.KAFKA_BROKER)
        )
        await producer.start()
        return producer

    async def send_message(self, topic: bytes, message: bytes):

        if not self.producer:
            logger.info("Kafka producer is not running")
            self.producer = await self.producer_start()

        try:
            logger.info("Try to send message to kafka")
            await self.producer.send_and_wait(topic, message)

        except Exception as e:
            logger.error("Can not send message to kafka")
            logger.error(e)
            raise e

    async def stop(self):
        logger.info("Stop kafka producer")
        await self.producer.stop()

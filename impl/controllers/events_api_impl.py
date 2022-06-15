import logging
from collector.libs import config_loader

logger = logging.getLogger(__name__)
config = config_loader.Config()


class EventsApi:
    def __init__(self, config, kafka_client):
        self.config = config
        self.kafka_client = kafka_client

    async def receive_raw_event(self, event_id: int, source: str, created: str, payout: int, *args):
        logger.info(f"{event_id=} {source=} {created=} {payout=}")

        return {"status": "OK"}
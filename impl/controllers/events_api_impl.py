import logging
import json

from fastapi import HTTPException, status as HTTP_status

from libs import config_loader, metrics
from libs.logger_colorer import colored_stream
from models.raw_event import RawEvent


config = config_loader.Config()
logging.basicConfig(
    level=logging.getLevelName(config.get(config_loader.LOGGING_LEVEL)),
    format=config.get(config_loader.LOGGING_FORMAT),
    handlers=[
        colored_stream,
    ],
)
logger = logging.getLogger(__name__)


class EventsApi:
    def __init__(self, config, kafka_client):
        self.config = config
        self.kafka_client = kafka_client

    async def receive_raw_event(self, source: str, event_name: str, event_status: str, created: str, payout: int):
        raw_event = RawEvent(
            source=source,
            event_name=event_name,
            event_status=event_status,
            created=created,
            payout=payout
        )
        logger.info(f"Received event: {raw_event=}")

        await self.send_raw_event_to_kafka(raw_event)

        return {"status": "OK"}
    

    async def send_raw_event_to_kafka(self, raw_event: RawEvent) -> bool:
        topic = self.config.get(config_loader.RAW_EVENTS_TOPIC)
        logger.info(f"Sending event to kafka: {raw_event=} {topic=}")

        try:
            serialized_event = json.dumps(raw_event.dict()).encode()
            await self.kafka_client.send_message(
                topic=topic,
                message=serialized_event
            )
            logger.info("Event sent successfully")
        
        except Exception as exc:
            logger.error(f"Sending {raw_event=} to {topic} failed")
            logger.error(f"{str(exc)}")
            raise HTTPException(
                status_code=HTTP_status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc)
            ) from exc


        return True
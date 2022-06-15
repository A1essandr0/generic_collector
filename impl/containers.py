from dependency_injector import containers, providers

from collector.libs import config_loader
from collector.libs.kafka_client import KafkaClient

from collector.controllers.events_api_impl import EventsApi


class Container(containers.DeclarativeContainer):
    # Service configuration
    config = config_loader.Config()

    kafka_client = providers.Singleton(KafkaClient, config=config)

    # API implementation
    events_collector_api = providers.Factory(
        EventsApi,
        config=config,
        kafka_client=kafka_client,
    )

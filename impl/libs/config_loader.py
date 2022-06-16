import os

from configloader import ConfigLoader

config_abs_path = "/".join(os.path.abspath(__file__).split("/")[0:-2])
SERVICE_NAME = "EVENTS_COLLECTOR"
ENV_CONFIG_PATH = os.getenv(f"{SERVICE_NAME}_CONFIG_PATH")


class Config:
    def __init__(self, config_file_path=os.path.join(config_abs_path, "config.yml")):
        self.config_loader = ConfigLoader()
        if ENV_CONFIG_PATH:
            # print(f"Use config file from env: {ENV_CONFIG_PATH}")
            self.config_loader.update_from_yaml_file(ENV_CONFIG_PATH)
        else:
            # print(f"Use default config file: {config_file_path}")
            self.config_loader.update_from_yaml_file(config_file_path)
        self.config_loader.update_from_env_namespace(f"{SERVICE_NAME}")

    def get(self, setting_name):
        return self.config_loader.get(setting_name, None)

    def to_dict(self):
        loader = self.config_loader
        return {key: loader.get(key) for key in loader.keys()}


LOGGING_LEVEL = "LOGGING_LEVEL"
LOGGING_FORMAT = "LOGGING_FORMAT"

KAFKA_BROKER = "KAFKA_BROKER"
RAW_EVENTS_TOPIC = "RAW_EVENTS_TOPIC"

API_KEY = "API_KEY"

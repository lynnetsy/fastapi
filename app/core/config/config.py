from app.core.config.app_config import AppConfig
from app.core.config.db_config import DbConfig


class Config:
    _instance = None

    app: AppConfig
    db: DbConfig

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def load(self, config: dict) -> None:
        self.app = AppConfig(
            **config["app"]
        )
        self.db = DbConfig(
            **config["db"]
        )
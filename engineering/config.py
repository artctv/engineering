import os
from pydantic import BaseSettings
from pathlib import Path


class RedisSettings(BaseSettings):
    host: str = os.getenv("redis_host") or "0.0.0.0"
    port: int = 6379
    db: int = 0
    password: str = 'password'


class ApiSettings(BaseSettings):
    title: str = "API"
    description: str = "Simple API with ML model"
    version: str = "0.0.1"

    host: str = os.getenv("host") or "127.0.0.1"
    port: int = 5000
    reload: bool = os.getenv("reload") or True

    origins: list[str] = [
        "http://localhost",
        "http://localhost:5000",
        "http://127.0.0.1",
        "http://127.0.0.1:5000",
    ]


class WorkerSettings(BaseSettings):
    queues: list[str] = ["default"]
    tasks: dict[str, str] = {
        "call_model": "worker.tasks.call_model",
    }


class Settings(BaseSettings):
    base_dir: Path = Path(__file__).parent.parent
    image_dir_name: str = "images"
    time_delay: int = 15

    redis: RedisSettings = RedisSettings()
    api: ApiSettings = ApiSettings()
    worker: WorkerSettings = WorkerSettings()

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '__'


settings: Settings = Settings()

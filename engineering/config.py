from pydantic import BaseSettings


class RedisSettings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 6379
    db: int = 0

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class Settings(BaseSettings):
    # FastAPI app params
    title: str = "API"
    description: str = "Simple API with ML model"
    version: str = "0.0.1"

    # run params
    host: str = "127.0.0.1"
    port: int = 5000
    reload: bool = True

    # API core params
    origins: list[str] = [
        "http://localhost",
        "http://localhost:5000",
        "http://127.0.0.1",
        "http://127.0.0.1:5000",
    ]

    # redis connection
    redis: RedisSettings = RedisSettings()

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings: Settings = Settings()

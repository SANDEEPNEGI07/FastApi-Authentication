from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    # Database related
    db_host: str
    db_port: int
    db_name: str
    db_password: str
    db_user: str
    port: str

    #JWT Token Related
    secret_key: str
    refresh_secret_key: str
    algorithm: str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    REFRESH_TOKEN_EXPIRE_MINUTES: int

    #internal .env
    adminapikey: str

    SERVER: str

    class config:
        env_file = Path(Path(__file__).resolve().parent) / ".env"
        print(f"environment created - {Path(Path(__file__).resolve().name)}")

setting = Settings()
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str

    class Comfig:
        env_file = '.env'


settings = Settings()

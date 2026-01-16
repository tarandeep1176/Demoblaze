import os
import dotenv

dotenv.load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL")
    APP_USERNAME = os.getenv("APP_USERNAME")
    APP_PASSWORD = os.getenv("APP_PASSWORD")

    print(APP_USERNAME)
    print(APP_PASSWORD)
    print(BASE_URL)
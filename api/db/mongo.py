from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticDatabase
from urllib.parse import quote_plus


def get_database(env) -> AgnosticDatabase:
    database = env.get('MONGO_DATABASE', default='app_db')
    username = env.get('MONGO_USERNAME', default='root')
    password = env.get('MONGO_PASSWORD', default='root')
    mongo_uri = env.get('MONGO_URI', default='localhost:27017')
    
    # URL encode username and password to handle special characters
    username = quote_plus(username)
    password = quote_plus(password)
    
    connection_string = f"mongodb://{username}:{password}@{mongo_uri}/"

    client = AsyncIOMotorClient(connection_string)
    return client[database]

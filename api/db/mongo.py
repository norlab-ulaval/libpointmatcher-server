from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticDatabase
from urllib.parse import quote_plus

def get_database(env) -> AgnosticDatabase:
    database = env['MONGO_DATABASE']
    username = env['MONGO_USERNAME']
    password = env['MONGO_PASSWORD']
    
    # URL encode username and password to handle special characters
    username = quote_plus(username)
    password = quote_plus(password)
    
    connection_string = f"mongodb://{username}:{password}@mongo:27017/"

    client = AsyncIOMotorClient(connection_string)
    return client[database]

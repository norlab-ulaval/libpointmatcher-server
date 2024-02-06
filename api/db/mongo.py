from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticDatabase


def get_database(env) -> AgnosticDatabase:
    database = env['MONGO_DATABASE']
    username = env['MONGO_USERNAME']
    password = env['MONGO_PASSWORD']
    
    connection_string = "mongodb://${USERNAME}:${PASSWORD}@mongo:27017/".format(
        USERNAME=username, PASSWORD=password
    )

    client = AsyncIOMotorClient(connection_string)
    return client[database]

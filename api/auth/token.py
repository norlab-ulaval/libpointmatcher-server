import os

import redis
from datetime import datetime, timedelta
from jose import jwt, JWTError
from interface.interface_models import TokenData

ACCESS_TOKEN_EXPIRE_MINUTES = 60
SECRET_KEY = "faudrait générer une clé"
ALGORITHM = "HS256"

redis_client = redis.Redis(host=os.environ.get("REDIS_URI", "localhost"), port=6379, db=0, password="potato123")


def create_access_token(user) -> str:
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": user.username}.copy()

    expire = datetime.utcnow() + access_token_expires
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    redis_client.set(user.username, encoded_jwt, ex=access_token_expires)

    return encoded_jwt


def get_validated_tokenData(token: str) -> TokenData | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None

        token = redis_client.get(username)
        if token is None:
            return None

        return TokenData(username=username)

    except JWTError:
        return None

import os

import redis
from datetime import datetime, timedelta
from jose import jwt, JWTError
from interface.interface_models import User

ACCESS_TOKEN_EXPIRE_MINUTES = 2
SECRET_KEY = "faudrait générer une clé"
ALGORITHM = "HS256"

redis_client = redis.Redis(host=os.environ.get("REDIS_URI", "localhost"), port=6379, db=0, password="potato123")


def create_access_token(user: User) -> str:
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": user.email}.copy()

    expire = datetime.utcnow() + access_token_expires
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    redis_client.set(user.email, encoded_jwt, ex=access_token_expires)

    return encoded_jwt


def get_validated_email(token: str) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            return None

        token = redis_client.get(email)
        if token is None:
            return None

        return email

    except JWTError:
        return None
    

def remove_token(email: str) -> bool | None:
    if not redis_client.exists(email):
        return None

    try:
        redis_client.delete(email)
        return True
    except Exception:
        return None

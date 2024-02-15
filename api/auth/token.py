from datetime import datetime, timedelta
from jose import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 60
SECRET_KEY = "faudrait générer une clé"
ALGORITHM = "HS256"

def create_access_token(user) -> str:
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": user.username}.copy()

    expire = datetime.utcnow() + access_token_expires
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

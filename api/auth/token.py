from datetime import timedelta
import datetime
from jose import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 60
SECRET_KEY = "faudrait générer une clé"
ALGORITHM = "HS256"

def create_access_token(self, user):
    access_token_expires = timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": user.username}.copy()

    expire = datetime.utcnow() + access_token_expires
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": encoded_jwt, "token_type": "bearer"}
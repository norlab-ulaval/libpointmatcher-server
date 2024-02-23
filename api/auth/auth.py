from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jwt
from interface.interface_models import UserInDB, TokenData
from database import db
from auth.token import get_validated_tokenData

SECRET_KEY = "faudrait générer une clé"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data)

def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    
    token_data: TokenData = get_validated_tokenData(token)
    if token_data is None:
        raise credential_exception

    user = get_user(db, username=token_data.email) # TODO: connect with user_controler to get user from db
    if user is None:
        raise credential_exception

    return user
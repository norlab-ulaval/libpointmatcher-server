from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
    email: str | None = None

class RegisteringUser(BaseModel):
    username: str
    email: str
    password: str

class LoginUser(BaseModel):
    username: str
    password: str

class User(BaseModel):
    username: str or None = None
    email: str

class UserInDB(User):
    hashed_password: str
    # yaml configs??

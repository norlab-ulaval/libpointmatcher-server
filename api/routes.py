from fastapi import FastAPI, Header, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from datetime import timedelta
from auth.auth import register, authenticate_user, create_access_token, oauth2_scheme
from interface.InterfaceModels import Token, RegisteringUser
from database import db

ACCESS_TOKEN_EXPIRE_MINUTES = 60

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello_world():
    return {"Hello": "World"}

@app.post("/register")
def register_user(user: RegisteringUser):
    register(user.username, user.email, user.password)
    
    return {"message": "User registered successfully",
            "user": user}

@app.post("/login", response_model=Token)
async def login_for_access_token(form_data: RegisteringUser):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/configs")
def get_configs(x_token: Annotated[str | None, Header(), Depends(oauth2_scheme)] = None):
    return {"configs": "configs"}
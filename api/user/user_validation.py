import re
from fastapi import HTTPException, status

# Email pattern : "string with maj, lower, numbers and some symbols" @ "string with maj, lower, numbers" . "maj or lower at least 2 long"
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# Username pattern : at least 2 characters
username_pattern = r'.{2,}'
# Password pattern : 8 characters at least, numbers, upper case and lower case letter, special character
password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&()])[A-Za-z\d@$!%*?&()]{8,}$'
    
def validate_email(email):
    return re.match(email_pattern, email) is not None

def validate_username(username):
    return re.match(username_pattern, username) is not None

def validate_password(password):
    return re.match(password_pattern, password) is not None

def validate(username: str, email: str, password: str) -> None:
    if not validate_email(email):
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = "Email is not valid")
    if not validate_username(username):
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = "Username is not valid")
    if not validate_password(password):
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = "Password must be at least 8 characters, with a number, an upper case, a lower" +
                            " case and a special character")
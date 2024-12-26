from datetime import datetime, timedelta, timezone
import  jwt 
from jwt.exceptions import InvalidTokenError
from blog.schemes import TokenData
# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "6e340aa1fb081ca5dbfb5b5c53013a67b2f47459e3a74018088160dd708816b8"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
        return token_data
    except InvalidTokenError:
        raise credentials_exception



   



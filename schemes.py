from pydantic import BaseModel
from typing import List

# class UserRequest(BaseModel):
#     user_name:str
#     password:str


class Users(BaseModel):
    username:str
    email:str
    password:str


class ShowUsers(BaseModel):
    username:str
    email:str

    class Config():
        orm_mode=True
        from_attributes =True


class blog(BaseModel):
    title:str
    body:str
    class Config():
        orm_mode=True
        from_attributes =True

class ShowUsersWithBlogs(BaseModel): 
    username: str 
    email: str 
    blogs: List[blog] =[]
    class Config: 
        orm_mode =True
        from_attributes =True

class Blogdata(BaseModel):
    title:str
    body:str
    owner_id:ShowUsers
    class Config: 
        orm_mode = True 
        from_attributes =True


class login(BaseModel):
    email:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
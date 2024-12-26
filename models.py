from blog.database import Base

from sqlalchemy import String,Column,Integer,ForeignKey

class Userss(Base):
    __tablename__='created_user'
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(50))
    email=Column(String(50),unique=True)
    password=Column(String(256))

class Blog(Base):
    __tablename__='blogs'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(50))
    body=Column(String(50))
    owner_id=Column(Integer,ForeignKey("created_user.id"))
    


# class Users(Base):
#     __tablename__='users'
#     id=Column(Integer,primary_key=True,index=True)
#     user_name=Column(String(50))
#     hashed_password=Column(String(200))


from fastapi import Depends, APIRouter,status,Response,HTTPException
from blog import schemes,models,database
from sqlalchemy.orm import Session
from blog.hashing import Hash
from typing import List


router=APIRouter(prefix='/user',tags=['user'])


@router.post('/',response_model=schemes.ShowUsers, status_code=status.HTTP_201_CREATED)
def create_user(request:schemes.Users,db:Session=Depends(database.get_db)):
    data=db.query(models.Userss).filter(models.Userss.email==request.email).first()
    if not data:
        hashpassword=Hash.decrypt(request.password)
        new_user=models.Userss(username=request.username,email=request.email,password=hashpassword)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return schemes.ShowUsers(username=request.username,email=request.email)
    else:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail='Email already exists')

@router.get('/{id}', response_model=schemes.ShowUsersWithBlogs)
def get_users(id: int, db: Session = Depends(database.get_db)): 
    user = db.query(models.Userss).filter(models.Userss.id == id).first() 
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found") 
    blogs = db.query(models.Blog).filter(models.Blog.owner_id == id).all() 
    blogs_list = [schemes.blog.from_orm(blog) for blog in blogs] 
    return schemes.ShowUsersWithBlogs(username=user.username, email=user.email, blogs=blogs_list)
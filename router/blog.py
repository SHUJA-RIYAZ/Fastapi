from fastapi import Depends, APIRouter,status,Response,HTTPException
from blog import schemes,models,database,oauth2,Token
from sqlalchemy.orm import Session
from typing import List
from blog.repository import blog

router=APIRouter(
    prefix='/blog',
    tags=['blog'])


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schemes.blog , db:Session=Depends(database.get_db),current_user:schemes.Users=Depends(oauth2.get_current_user)):
        return blog.create(db,request)
   



@router.get('/', response_model=List[schemes.Blogdata])
def get_blogs(db: Session = Depends(database.get_db),current_user:schemes.Users=Depends(oauth2.get_current_user)):
   return blog.get_all(db)



@router.get('/{id}',status_code=200,response_model=schemes.Blogdata)
def get_blog(id:int,db:Session=Depends(database.get_db),current_user:schemes.Users=Depends(oauth2.get_current_user)):
   return blog.get_by_id(id,db)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int,db:Session=Depends(database.get_db),current_user:schemes.Users=Depends(oauth2.get_current_user)):
    return blog.delete(id,db)



@router.put('/{id}')
def update_blog(id:int,request:schemes.blog,db:Session=Depends(database.get_db),current_user:schemes.Users=Depends(oauth2.get_current_user)):
    if (db.query(models.Blog).filter(models.Blog.id==id).first()):
        db.query(models.Blog).filter(models.Blog.id==id).update(request.dict())
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Blog with the id {id} is not found")
    db.commit()
    return 'updated'
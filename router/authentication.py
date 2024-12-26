from fastapi import Depends, APIRouter,status,HTTPException
from blog import schemes,database
from sqlalchemy.orm import Session
from blog.models import Userss
from blog.hashing import Hash
from datetime import  timedelta
from blog.Token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user=db.query(Userss).filter(Userss.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                            detail=f'Invalid email')
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid Password')
    # return create_access_token(data={"sub": user.email})
    access_token=create_access_token(data={"email": user.email})
    return {"access_token":access_token, "token_type":"bearer"}


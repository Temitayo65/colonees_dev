from typing import List, Optional
from fastapi.security import OAuth2PasswordRequestForm
import sqlalchemy
from .. import schemas, models, utils
from fastapi.params import Depends
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, HTTPException
from .. import oauth2


router = APIRouter(
    prefix="/admin-user"
)

@router.post("/login", response_model=schemas.Token)
async def login(admin_user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.AdminUser).filter(
        models.AdminUser.email == admin_user_credentials.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not utils.verify(admin_user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    # create a token
    access_token = oauth2.create_access_token(data={"email": user.email})
    # return token
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/all-users", response_model=List[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    if not current_user.is_authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required"
        )
    users = db.query(models.User).all()
    [user.__dict__.pop("password") for user in users] # removes password from users 
    all_users = [
        schemas.UserResponse(
            email=user.email,
            is_talent=user.is_talent,
            is_business=user.is_business,
            subscribed=user.subscribed
        )
        for user in users
    ]

    return all_users  


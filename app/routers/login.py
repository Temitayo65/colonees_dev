from typing import List, Optional
from .. import schemas, models, utils, oauth2
from fastapi.params import Depends
from ..database import get_db
from sqlalchemy.orm import Session 
from fastapi import security, security, security, security, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import APIRouter, HTTPException,status
from ..models import User


router = APIRouter(
    prefix="/login", 
    tags=["Authentication"]
)


@router.post("/", response_model=schemas.Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session=Depends(get_db) ):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")
    
    # create a token 
    access_token = oauth2.create_access_token(data= {"email":user.email})
    # return token 
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/talent-users", response_model=schemas.TalentProperUserResponse)
def get_users(db:Session = Depends(get_db), current_user: str=Depends(oauth2.get_current_user),limit: int = 3, skip: int = 0, search: Optional[str] = ""):
    if not current_user.is_authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required"
        )
    users = db.query(models.TalentUser).filter(models.TalentUser.role.contains(search)).limit(limit).offset(skip).all()
    [user.__dict__.pop("password") for user in users] # this gets each dictionary from the "users" table and removes the password before returning the response 
    talent_users = [
        schemas.TalentProperUserResponse(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone_number=user.phone_number,
            role=user.role,
            subscribed=user.subscribed,
            portfolio_link=user.portfolio_link
        )
        for user in users
    ]
    
    return talent_users # this does not contain the passwords
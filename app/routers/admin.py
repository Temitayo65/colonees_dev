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
async def get_all_users(db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
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


@router.post("/admin-rights")
async def give_admin_rights(newAdminUser: schemas.AdminUser, current_user: str = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    if not current_user.is_authenticated:
       raise HTTPException(
           status_code=status.HTTP_401_UNAUTHORIZED,
           detail="Authentication required"
       )
    
    # check to see if the user already exists 
    existing_user = db.query(models.AdminUser).filter(
        models.AdminUser.email == newAdminUser.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"User with email: {newAdminUser.email} already exists")
    
    # check to see if the current user is a master Admin user(check this state in the database)
    is_master_user = db.query(models.AdminUser).filter(models.AdminUser.email == current_user.email).first()
    
    if is_master_user != None: 
        if is_master_user.is_master:
            # add to admin table
            try:
                user = models.AdminUser(**newAdminUser.model_dump())
                user.password = utils.hash(newAdminUser.password)
                db.add(user)
                db.commit()
                db.refresh(user)
                return {"message": f"user with email: {user.email}, successfully added as Admin"}
            
            except sqlalchemy.exc.IntegrityError as e:
                db.rollback()
                if "duplicate key" in str(e):
                    raise HTTPException(status_code=status.HTTP_302_FOUND,
                                        detail=f"{user.business_name} is already an Admin")
                else:
                    raise HTTPException(
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Only master admins can make others admin")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"This user is not an admin user")
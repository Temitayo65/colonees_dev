import sqlalchemy
from .. import schemas, models, utils
from fastapi.params import Depends
from ..database import get_db
from sqlalchemy.orm import Session 
from fastapi import APIRouter,status, HTTPException


router = APIRouter(
    prefix="/api"
)

@router.post("/business-waitlist", status_code=status.HTTP_201_CREATED, tags=["WaitList"])
async def join_business_waitlist(user: schemas.BusinessWaitListUserCreate, db: Session =Depends(get_db)):
    existing_user = db.query(models.BusinessWaitlistUser).filter(models.BusinessWaitlistUser.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with email: {user.email} already exists")
    try:
        business_waitlist_user = models.BusinessWaitlistUser(**user.model_dump())
        db.add(business_waitlist_user)
        db.commit()
        db.refresh(business_waitlist_user)
        return {"message": " successfully joined business waitlist"}
    except sqlalchemy.exc.IntegrityError as e:
        db.rollback()
        if "duplicate key" in str(e):
            raise HTTPException(status_code=status.HTTP_302_FOUND, detail=f"{user.business_name} is already on the business waitlist")
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")



@router.post("/users/join-business", status_code=status.HTTP_201_CREATED, tags=["Join"])
async def create_business_user(user: schemas.BusinessProperUserCreate, db: Session =Depends(get_db)):
    existing_user = db.query(models.BusinessUser).filter(models.BusinessUser.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with email: {user.email} already exists")
    business_user = models.BusinessUser(**user.model_dump())
    try:
        # adding the data to the "business_users" table 
        db.add(business_user)
        db.commit()
        db.refresh(business_user)

        # adding parts of the data to the "users" table for easy login authentication from the "users" table
        user_table_addition = models.User()  # creates an instance of the model table to be filled with relevant data 
        user_table_addition.is_business = True
        user_table_addition.email = user.email
        user_table_addition.subscribed = user.subscribed
        user_table_addition.password = utils.hash(user.password)
        db.add(user_table_addition)
        db.commit()
        db.refresh(user_table_addition)
        return {"message": "successfully joined business list"}
    
    except sqlalchemy.exc.IntegrityError as e:
        db.rollback()
        if "duplicate key" in str(e):
            raise HTTPException(status_code=status.HTTP_302_FOUND, detail=f"{user.business_name} is already on the business list")
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

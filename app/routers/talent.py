from fastapi import APIRouter,status, HTTPException
import sqlalchemy
from .. import schemas, models, utils
from fastapi.params import Depends
from ..database import  get_db
from sqlalchemy.orm import Session 


router = APIRouter(
    prefix="/api"
)

@router.post("/talent-waitlist", status_code=status.HTTP_201_CREATED, tags=["WaitList"])
async def join_talent_waitlist(user: schemas.TalentWaitListUserCreate, db: Session =Depends(get_db)):
    existing_user = db.query(models.TalentWaitlistUser).filter(models.TalentWaitlistUser.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with email: {user.email} already exists")
    try:
        talent_waitlist_user = models.TalentWaitlistUser(**user.model_dump())
        db.add(talent_waitlist_user)
        db.commit()
        db.refresh(talent_waitlist_user)
        return {"message": " successfully joined talent waitlist"}
    
    except sqlalchemy.exc.IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@router.post("/users/join-talent", status_code=status.HTTP_201_CREATED, tags=["Join"])
async def create_talent_user(user: schemas.TalentProperUserCreate, db: Session =Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with email: {user.email} already exists")
    
    # hashing the password before saving the data in the talent_users table in the database 
    hashed_password = utils.hash(user.password) # a negligible error messsage is shown in the terminal
    user.first_name, user.last_name = user.first_name.capitalize(), user.last_name.capitalize()
    user.password = hashed_password # changes the password in the database to be a hash value 
    new_talent_user = models.TalentUser(**user.model_dump())

    try:
        db.add(new_talent_user)
        db.commit()
        db.refresh(new_talent_user)

        # adding parts of the payload to the users table in the database 
        user_table_addition = models.User()  # creates an instance of the model table to be filled with relevant data 
        user_table_addition.is_talent = True
        user_table_addition.email = user.email
        user_table_addition.subscribed = user.subscribed
        user_table_addition.password = hashed_password
        db.add(user_table_addition)
        db.commit()
        db.refresh(user_table_addition)
        return {"message": " successfully joined talent list"}
    
    except sqlalchemy.exc.IntegrityError as e:
        db.rollback()
        if "duplicate key" in str(e):
            raise HTTPException(status_code=status.HTTP_302_FOUND, detail=f"{user.business_name} is already on the business list")
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")


from fastapi import APIRouter, status, HTTPException
import sqlalchemy
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi.params import Depends

router = APIRouter(
    prefix="/api",
    tags=["Subscribe"]
)

# For joining the initial subscription table 
@router.post("/subscribe", status_code=status.HTTP_201_CREATED)
async def join_subscribers(user: schemas.SubsriberUserCreate, db: Session=Depends(get_db)):
    try:
        # Create an instance of the Subscriber model without providing an explicit id
        new_subscriber = models.Subscriber(email=user.email)
        db.add(new_subscriber)
        db.commit()
        db.refresh(new_subscriber)
        return {"message": f"{user.email} successfully subscribed"}
    except sqlalchemy.exc.IntegrityError as e:
        db.rollback()
        if "duplicate key" in str(e):
            raise HTTPException(status_code=status.HTTP_302_FOUND, detail=f"{user.email} is already subscribed")
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")


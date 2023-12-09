from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class BusinessWaitListUserCreate(BaseModel):
    email: EmailStr
    full_name : str
    business_name : str
    business_industry: str 
    subscribed : bool

class TalentWaitListUserCreate(BaseModel):
    email: EmailStr
    full_name : str
    industry : str
    designation : str
    subscribed : bool

class SubsriberUserCreate(BaseModel):
    email: EmailStr


class BusinessProperUserCreate(BaseModel): # this design is yet to be done by Pearl's Team
    full_name: str 
    business_name: str 
    email: EmailStr 
    password: str 
    business_industry: str 
    business_link: Optional[str]
    subscribed: bool

class BusinessProperUserResponse(BaseModel): # this design is yet to be done by Pearl's Team
    first_name: str
    last_name: str 
    business_name: str
    email: EmailStr
    industry: str

    class Config:
        from_attributes = True 


class TalentProperUserCreate(BaseModel):
    first_name: str
    last_name: str 
    email: EmailStr 
    password: str 
    phone_number: str 
    role: str 
    subscribed: Optional[bool] = False
    portfolio_link: Optional[str]


class TalentProperUserResponse(BaseModel):
    first_name: str
    last_name: str 
    email: EmailStr
    phone_number: str 
    role: str 
    portfolio_link: Optional[str] = None 
    subscribed: bool

    class Config:
        from_attributes = True 


class UserLogin(BaseModel):
    email: EmailStr
    password: str 


class Token(BaseModel):
    access_token : str 
    token_type: str 

class TokenData(BaseModel):
    email: str 
    is_authenticated: bool 



class UserResponse(BaseModel):
    id : int 
    email : str
    is_talent : bool
    is_business : bool
    subscribed : bool

    class Config:
        from_attributes = True 








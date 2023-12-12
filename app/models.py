from sqlalchemy import Column, Integer,String, TIMESTAMP,text, Boolean, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    email = Column(String, primary_key=True, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_talent = Column(Boolean,server_default="FALSE")
    is_business = Column(Boolean,server_default="FALSE")
    subscribed = Column(Boolean, default= False, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class TalentWaitlistUser(Base):
    __tablename__ = "talent_waitlist_users"
    email = Column(String, primary_key=True, nullable=False, unique=True)
    full_name = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    designation = Column(String, nullable=False)
    subscribed = Column(Boolean, default= False, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class BusinessWaitlistUser(Base):
    __tablename__ = "business_waitlist_users"
    full_name = Column(String, nullable=False)
    email = Column(String, primary_key=True, nullable=False, unique=True)
    business_name = Column(String, nullable=False, unique=True)
    business_industry = Column(String, nullable=False)
    business_link = Column(String, nullable=True)
    subscribed = Column(Boolean, server_default="FALSE", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
class TalentUser(Base):
    __tablename__ = "talent_users"
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, primary_key=True, nullable=False, unique=True)
    password = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    role = Column(String, nullable=False)
    portfolio_link = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    subscribed = Column(Boolean, default= False, nullable=False)

class BusinessUser(Base):
    __tablename__ = "business_users"
    full_name = Column(String, nullable=False)
    email = Column(String, primary_key=True, nullable=False, unique=True)
    password = Column(String, nullable=False)
    business_name = Column(String, nullable=False, unique=True)
    business_industry = Column(String, nullable=False)
    business_link = Column(String, nullable=True)
    subscribed = Column(Boolean, server_default="FALSE", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))  

class Subscriber(Base):
    __tablename__ = "subscribers"
    email = Column(String, nullable=False, primary_key= True, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    

class AdminUser(Base):
    __tablename__ = "administrators"
    email = Column(String, primary_key=True, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_master = Column(Boolean, default=False, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

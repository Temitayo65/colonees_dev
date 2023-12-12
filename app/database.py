from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
from . import utils, models




SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def initialize_admin_user(db_session):
    # Check if the admin user exists
    admin_user = db_session.query(models.AdminUser).filter_by(
        models.AdminUser.email =="iloritemitayo75@gmail.com").first()

    if not admin_user:
        # Create the admin user
        admin_user = models.AdminUser(email="iloritemitayo75@gmail.com",
                          password=utils.hash(settings.database_password), is_admin=True)
        db_session.add(admin_user)
        db_session.commit()

def get_db():
    db = SessionLocal()
    try: 
        initialize_admin_user(db)
        yield db 
    finally:
        db.close()

    

import database as _db
import sqlalchemy.orm as _orm
import models as _models
import schemas as _schemas

def create_database():
    return _db.Base.metadata.create_all(bind=_db.engine)

def get_db():
    db=_db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_by_email(db: _orm.Session, email:str):
    return db.query(_models.User).filter(_models.User.email == email).first()

def create_user(db:_orm.Session, user:_schemas.UserCreate):
    fake_hash = user.password + 'hashed'
    db_user = _models.User(email=user.email, hash_pass=fake_hash, first_name=user.first_name, last_name=user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db:_orm.Session, skip:int, limit:int):
    return db.query(_models.User).offset(skip).limit(limit).all()

def get_user(db:_orm.Session, user_id: int):
    return db.query(_models.User).filter(_models.User.id == user_id).first()
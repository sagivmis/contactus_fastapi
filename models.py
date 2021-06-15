import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import datetime as _dt

import database as _database

class User(_database.Base):
    __tablename__ = "users"
    id =_sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    hash_pass = _sql.Column(_sql.String)
    is_active = _sql.Column(_sql.Boolean, default=True)
    first_name = _sql.Column(_sql.String, index=True)
    last_name = _sql.Column(_sql.String, index=True)

    posts = _orm.relationship("Post", back_populates="owner")

class Post(_database.Base):
    __tablename__="posts"
    id=_sql.Column(_sql.Integer, primary_key=True, index=True)
    title = _sql.Column(_sql.String, index=True)
    content = _sql.Column(_sql.String, index=True)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    owner = _orm.relationship("User", back_populates="posts")
import pydantic as _pydantic
import datetime as _dt
from typing import List

class _PostBase(_pydantic.BaseModel):
    title: str
    content: str


class PostCreate(_PostBase):
    pass

class Post(_PostBase):
    id: int
    owner_id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True

class _UserBase(_pydantic.BaseModel):
    email:str

class UserCreate(_UserBase):
    password: str
# {
#   "email": "sagiv@gmail.com",
#   "id": 1,
#   "is_active": true,
#   "posts": []
# }
class User(_UserBase):
    id: int
    is_active: bool
    posts: List[Post] = []

    class Config:
        orm_mode = True

    #
    # {
    #     "id": 1,
    #     "owner_id": 23,
    #     "title":"this is a title",
    #     "content":"this is the post content",
    #     "date_created":"12-12-12",
    #     "date_last_updated":"12-12-12"
    # }
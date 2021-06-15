from typing import List
import fastapi as _fastapi
import uvicorn as _uvi
from fastapi.middleware.cors import CORSMiddleware

import services as _services
import schemas as _schemas
import sqlalchemy.orm as _orm
app= _fastapi.FastAPI()

_services.create_database()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    _uvi.run("main:app", host="0.0.0.0", port=8000, reload=True)

@app.get('/', tags=["Root"])
def read_root():
    return {
        "message": "Hello"
    }
@app.post('/users', response_model=_schemas.User, tags=["Users"])
def create_user(user: _schemas.UserCreate, db: _orm.Session=_fastapi.Depends(_services.get_db)):
     db_user = _services.get_user_by_email(db=db, email=user.email)
     if db_user:
         raise _fastapi.HTTPException(status_code=400, detail="the email is in use")
     return _services.create_user(db=db, user=user)

@app.get('/users', response_model=List[_schemas.User], tags=["Users"])
def get_users(skip: int=0, limit:int=10, db: _orm.Session=_fastapi.Depends(_services.get_db)):
    return _services.get_users(db=db,skip=skip,limit=limit)

@app.get('/users/{user_id}', response_model=_schemas.User, tags=["Users"])
def get_user_by_id(user_id:int, db: _orm.Session=_fastapi.Depends(_services.get_db)):
    db_user = _services.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise _fastapi.HTTPException(status_code=404, detail="sorry this user doesn't exist")
    return db_user
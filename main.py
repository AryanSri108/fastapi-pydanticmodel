# main.py
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional,List
from database import engine,sessionLocal,Base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import Session


#TODO: creating table or model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    password = Column(String,unique=True)
    address = Column(String)

#TODO: creating schema
class UserSchema(BaseModel):
    id:int
    name: str
    age: int
    password: str
    address: Optional[str] = None

    #to avoid error for returning orm object
    class Config:
        orm_mode=True

#TODO: now creating this model in database & this will create only for onetime
Base.metadata.create_all(engine)
app = FastAPI()

#for database connection or session --> it is a dependency
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

#TODO: insert record in table by using post method
@app.post("/users",response_model=UserSchema)
def index(user:UserSchema,db:Session=Depends(get_db)):
    #to put data in database
    userObject = User(id=user.id,name=user.name,age=user.age,password=user.password,address=user.address)
    db.add(userObject)
    db.commit() #because autocommit=False
    return userObject

@app.get("/users",response_model=List[UserSchema])
def index(db:Session=Depends(get_db)):
    #to get data from database
    return db.query(User).all()
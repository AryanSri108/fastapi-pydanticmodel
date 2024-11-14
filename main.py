# main.py
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import engine,sessionLocal,Base
from sqlalchemy import Column,Integer,String,Boolean

app = FastAPI()

#TODO: creating table 
class User(Base):
    __tablename__ = 'users' #syntax to create table in sqlalchemy
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

#TODO: now creating this model in database & this will create only for onetime
Base.metadata.create_all(engine)

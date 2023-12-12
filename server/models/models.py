from sqlalchemy import  Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from server.db.db import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    billing_address = Column(String,nullable=True)
    shipping_address = Column(String,nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
    
from sqlalchemy import Column, String, Integer
from ..database.core import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    password_hash = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<User(first_name='{self.first_name}', last_name= '{self.last_name}', email= '{self.email}')"
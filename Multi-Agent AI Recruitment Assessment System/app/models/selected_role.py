from sqlalchemy import Column, Integer, String
from app.database import Base

class SelectedRole(Base):
    __tablename__ = "selected_roles"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    role = Column(String)
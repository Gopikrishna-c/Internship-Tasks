from sqlalchemy import Column, Integer, String, Text
from .database import Base


class UserMemory(Base):

    __tablename__ = "user_memories"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        nullable=False,
        index=True
    )

    memory_type = Column(
        String,
        nullable=False
    )

    memory_value = Column(
        Text,
        nullable=False
    )
import uuid
from datetime import datetime
from sqlalchemy import Column, String, BigInteger, DateTime, JSON, Text
from sqlalchemy.dialects.postgresql import UUID
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    telegram_id = Column(BigInteger, unique=True, nullable=True)
    username = Column(String(255), nullable=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    photo_url = Column(Text, nullable=True)
    role = Column(String(50), default="user")
    status = Column(String(50), default="active")
    email = Column(String(255), unique=True, nullable=True)
    store_id = Column(String(255), nullable=True)
    orders_count = Column(BigInteger, default=0)
    last_order_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login_at = Column(DateTime, nullable=True)
    phone_number = Column(String(20), nullable=True)
    attribute = Column(JSON, nullable=True)
    password = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
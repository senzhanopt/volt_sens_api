from sqlalchemy import Column, Integer, Float, String, TIMESTAMP, func
from app.db import Base

class Measurement(Base):
    """Stores bus measurements."""
    __tablename__ = "measurements"

    id: int = Column(Integer, primary_key=True)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=func.now())
    bus_id: int = Column(String, index=True)
    p_mw: float = Column(Float, nullable=True)
    q_mvar: float = Column(Float, nullable=True)
    v_pu: float = Column(Float, nullable=True)
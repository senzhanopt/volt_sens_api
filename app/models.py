from sqlalchemy import TIMESTAMP, Column, Float, Integer, String, text

from app.db import Base


class Measurement(Base):
    """Stores bus measurements."""

    __tablename__ = "measurements"

    id: int = Column(Integer, primary_key=True)
    timestamp = Column(
        TIMESTAMP(timezone=True), server_default=text("timezone('UTC', now())")
    )
    bus_id: str = Column(String, index=True)
    p_kw: float = Column(Float, nullable=True)
    q_kvar: float = Column(Float, nullable=True)
    v_pu: float = Column(Float, nullable=True)

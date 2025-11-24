from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MeasurementIn(BaseModel):
    """
    Input schema for a bus measurement.
    """
    timestamp: Optional[datetime]
    bus_id: str
    p_kw: Optional[float] = None
    q_kvar: Optional[float] = None
    v_pu: Optional[float] = None

class MeasurementOut(BaseModel):
    """
    Output schema for a bus measurement.
    """
    id: int
    bus_id: str
    p_kw: Optional[float] = None
    q_kvar: Optional[float] = None
    v_pu: Optional[float] = None
    timestamp: Optional[datetime] = None

    class Config:
        orm_mode = True
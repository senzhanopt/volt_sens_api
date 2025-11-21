from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MeasurementIn(BaseModel):
    """
    Input schema for a bus measurement.
    Any of p_mw, q_mvar, or v_pu can be null.
    """
    timestamp: Optional[datetime]
    bus_id: str
    p_mw: Optional[float] = None
    q_mvar: Optional[float] = None
    v_pu: Optional[float] = None

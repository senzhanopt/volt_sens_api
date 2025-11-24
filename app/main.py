from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import insert
from typing import List, Dict

from app.db import Base, engine, get_session
from app.schemas import MeasurementIn
from app.models import Measurement


app = FastAPI(title = "Grid Measurement API Demo")

@app.get("/")
def index():
    """
    Root endpoint.
    """
    return {
        "message": "Welcome to the VoltSens API Demo!"
    }

@app.get("/meas", response_model=List[Dict])
def read_measurements(session: Session = Depends(get_session),
        limit: int = Query(100, description="Max number of rows to return")):
    """
    Query all measurements.
    """
    measurements = session.query(Measurement).limit(limit).all()
    # Convert SQLAlchemy objects to dictionaries for JSON
    result = [
        {
            "id": m.id,
            "bus_id": m.bus_id,
            "p_mw": m.p_kw,
            "q_mvar": m.q_kvar,
            "v_pu": m.v_pu,
            "timestamp": m.timestamp.isoformat() if m.timestamp else None
        }
        for m in measurements
    ]

    return result

@app.post("/meas")
def create_meas(meas: MeasurementIn, session: Session = Depends(get_session)):
    """
    Store a new measurement.
    """
    stmt = insert(Measurement).values(**meas.dict(exclude_unset=True))
    session.execute(stmt)
    session.commit()
    return {"status": "ok"}


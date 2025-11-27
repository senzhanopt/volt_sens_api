from typing import Dict, List

from fastapi import Body, Depends, FastAPI, HTTPException, Query
from sqlalchemy import delete, insert
from sqlalchemy.orm import Session

from app.db import get_session
from app.models import Measurement
from app.schemas import MeasurementIn, MeasurementOut

app = FastAPI(title="Grid Measurement API Demo")


@app.get("/")
def index():
    """
    Root endpoint.
    """
    return {"message": "Welcome to the VoltSens API Demo!"}


@app.post("/meas")
def create_measurement(meas: MeasurementIn, session: Session = Depends(get_session)):
    """
    Store a new measurement.
    """
    stmt = insert(Measurement).values(**meas.model_dump(exclude_unset=True))
    session.execute(stmt)
    session.commit()
    return {"status": "ok"}


@app.get("/meas", response_model=List[MeasurementOut])
def read_measurements(
    session: Session = Depends(get_session),
    limit: int = Query(100, description="Max number of rows to return"),
):
    """
    Query all measurements.
    """
    measurements = session.query(Measurement).limit(limit).all()

    return measurements


@app.delete("/meas/{meas_id}")
def delete_measurement(meas_id: int, session: Session = Depends(get_session)):
    """
    Delete a measurement.
    """
    measurement = session.query(Measurement).filter(Measurement.id == meas_id).first()
    if not measurement:
        raise HTTPException(status_code=404, detail="Measurement not found.")

    session.delete(measurement)
    session.commit()
    return {"status": "deleted", "id": meas_id}


@app.delete("/meas")
def delete_measurements(
    meas_ids: List[int] = Body(...), session: Session = Depends(get_session)
):
    """
    Delete measurements.
    """
    measurements = session.query(Measurement).filter(Measurement.id.in_(meas_ids)).all()

    if not measurements:
        raise HTTPException(status_code=404, detail="Measurements not found.")

    for meas in measurements:
        session.delete(meas)
        session.commit()

    deleted_ids = [meas.id for meas in measurements]
    return {"status": "deleted", "deleted_ids": deleted_ids}


@app.patch("/meas/{meas_id}", response_model=MeasurementOut)
@app.put("/meas/{meas_id}", response_model=MeasurementOut)
def update_measurement(
    meas_id: int,
    meas_update: MeasurementIn = Body(...),
    session: Session = Depends(get_session),
):
    """
    Update a measurement.
    """
    measurement = session.query(Measurement).filter(Measurement.id == meas_id).first()
    if not measurement:
        raise HTTPException(status_code=404, detail="Measurement not found.")

    for key, value in meas_update.model_dump(exclude_unset=True).items():
        setattr(measurement, key, value)

    session.commit()
    session.refresh(measurement)
    return measurement

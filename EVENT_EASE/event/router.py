from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dbmodel import get_db
from model import events, eventsPydantic

router = APIRouter()


@router.post("/events/", response_model=eventsPydantic)
def create_event(
    event_name: str,
    date: str,
    information: str,
    price: float,
    status: str,
    location: str,
    organizator_id:int, db: Session= Depends(get_db)):
    new_event = events(event_name=event_name,date=date , information=information,price=price,status=status,location=location,organizator_id=organizator_id)

    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return {"message": "Event successfully created","events":new_event}


@router.get("/events/", response_model=eventsPydantic)
def read_events(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(events).offset(skip).limit(limit).all()


@router.get("/events/{event_id}", response_model=eventsPydantic)
def read_event(event_id: int=None , db: Session = Depends(get_db)):
    if event_id:
       event = db.query(events).filter(events.event_id == event_id).first()
       if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
       return event
    else:
        event=db.query(events).all()
        return event


@router.put("/events/{event_id}", response_model=eventsPydantic)
def update_event(event_id: int,updated_event : eventsPydantic, db: Session = Depends(get_db)):
    db_event = db.query(events).filter(events.event_id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    for attr, value in updated_event.dict().items():
        setattr(db_event, attr, value)

    db.commit()
    db.refresh(db_event)
    return db_event


@router.delete("/events/{event_id}",response_model=eventsPydantic)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    db_event = db.query(events).filter(events.event_id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(db_event)
    db.commit()
    return {"message": "Event deleted"}


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import model
from dbmodel import get_db
from model import organizator
from model import organizatorPydantic

router = APIRouter()


@router.post("/organizators/", response_model=organizatorPydantic)
def create_organizator(
    user_id: str,
    user_name: str,
    db: Session = Depends(get_db)
):
    new_organizator = organizator(user_id=user_id, user_name=user_name)
    db.add(new_organizator)
    db.commit()
    db.refresh(new_organizator)
    return new_organizator

@router.get("/organizators/", response_model=organizatorPydantic)
def read_organizators(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(organizator).offset(skip).limit(limit).all()

@router.get("/organizators/{organizator_id}", response_model=organizatorPydantic)
def read_organizator(organizator_id: int, db: Session = Depends(get_db), ):
    organizator = db.query(model.organizator).filter(model.organizator.organizator_id == organizator_id).first()
    if organizator is None:
        raise HTTPException(status_code=404, detail="Organizator not found")
    return organizator

@router.put("/organizators/{organizator_id}", response_model=organizatorPydantic)
def update_organizator(organizator_id: int, updated_organizator: organizatorPydantic, db: Session = Depends(get_db)):
    db_organizator = db.query(organizator).filter(organizator.organizator_id == organizator_id).first()
    if db_organizator is None:
        raise HTTPException(status_code=404, detail="Organizator not found")
    for attr, value in updated_organizator.dict().items():
        setattr(db_organizator, attr, value)
    db.commit()
    db.refresh(db_organizator)
    return db_organizator

@router.delete("/organizators/{organizator_id}",response_model=organizatorPydantic)
def delete_organizator(organizator_id: int, db: Session = Depends(get_db)):
    db_organizator = db.query(organizator).filter(organizator.organizator_id == organizator_id).first()
    if db_organizator is None:
        raise HTTPException(status_code=404, detail="Organizator not found")
    db.delete(db_organizator)
    db.commit()
    return {"message": "Organizator deleted"}

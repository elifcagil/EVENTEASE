from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import model
from model import userPydantic
from model import user
from dbmodel import get_db

router = APIRouter()


@router.get("/user/",response_model = userPydantic)
def read_user(user_id: int = None, db: Session = Depends(get_db)):
    if user_id:
        user = db.query(model.user).filter(model.user.user_id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")
        return user
    else:
        users = db.query(model.user).all()
        return users


@router.post("/user/", response_model=userPydantic)
def create_user(
        username: str, userpassword:str , email: str, userxp:int, db: Session = Depends(get_db)
):
    new_user = user(
        user_name=username, user_password=userpassword, user_mail=email,user_xp=userxp
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User successfully added", "user": new_user}
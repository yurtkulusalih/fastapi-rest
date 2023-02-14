from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db


router = APIRouter()

@router.get("")
def get_comments(db: Session = Depends(get_db)):
    return {"detail": "Do you really think you're ready for these comments?"}
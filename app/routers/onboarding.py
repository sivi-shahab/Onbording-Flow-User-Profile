from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from typing import List


router = APIRouter(prefix="/onboarding", tags=["onboarding"])

@router.get("/flow", response_model=schemas.FlowVersion)
def get_active_flow(db: Session = Depends(get_db)):
    flow = crud.get_active_flow(db)
    if not flow:
        raise HTTPException(status_code=404, detail="No active flow")
    return flow

@router.get("/questions", response_model=List[schemas.Question])
def list_questions(db: Session = Depends(get_db)):
    flow = crud.get_active_flow(db)
    if not flow:
        raise HTTPException(status_code=404, detail="No active flow")
    return crud.get_questions_for_flow(db, flow.id)

@router.post("/users/{user_id}/answers", response_model=schemas.Answer)
def submit_answer(user_id: str, answer: schemas.AnswerCreate, db: Session = Depends(get_db)):
    # you may add branching logic here to decide next question
    return crud.record_answer(db, user_id, answer)

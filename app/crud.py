from sqlalchemy.orm import Session
from . import models, schemas
from uuid import uuid4

def get_active_flow(db: Session):
    return db.query(models.FlowVersion).filter_by(is_active=True).first()

def get_questions_for_flow(db: Session, flow_id: str):
    return (
        db.query(models.Question)
        .filter_by(flow_version_id=flow_id)
        .order_by(models.Question.display_order)
        .all()
    )

def create_user(db: Session, user_in: schemas.UserCreate):
    db_user = models.User(email=user_in.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def record_answer(db: Session, user_id: str, ans: schemas.AnswerCreate):
    db_ans = models.UserAnswer(
        user_id=user_id,
        question_id=ans.question_id,
        selected_option_id=ans.selected_option_id,
        answer_text=ans.answer_text,
        answer_number=ans.answer_number
    )
    db.add(db_ans)
    db.commit()
    db.refresh(db_ans)
    return db_ans

def get_user_answers(db: Session, user_id: str):
    return db.query(models.UserAnswer).filter_by(user_id=user_id).all()

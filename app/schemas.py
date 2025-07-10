from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class FlowVersion(BaseModel):
    id: UUID
    name: str
    is_active: bool

    class Config:
        orm_mode = True

class QuestionOption(BaseModel):
    id: UUID
    code: str
    text: str

    class Config:
        orm_mode = True

class Question(BaseModel):
    id: UUID
    code: str
    text: str
    type: str
    display_order: int
    options: Optional[List[QuestionOption]] = []

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: str

class User(BaseModel):
    id: UUID
    email: str
    created_at: datetime

    class Config:
        orm_mode = True

class AnswerCreate(BaseModel):
    question_id: UUID
    selected_option_id: Optional[UUID] = None
    answer_text: Optional[str] = None
    answer_number: Optional[float] = None

class Answer(BaseModel):
    id: UUID
    user_id: UUID
    question_id: UUID
    selected_option_id: Optional[UUID]
    answer_text: Optional[str]
    answer_number: Optional[float]
    answered_at: datetime

    class Config:
        orm_mode = True

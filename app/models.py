import uuid
from sqlalchemy import (
    Column, String, Text, Integer, Boolean,
    ForeignKey, DateTime, JSON, Numeric
)
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from .database import Base
from datetime import datetime

class FlowVersion(Base):
    __tablename__ = "flow_versions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    is_active = Column(Boolean, default=False)

class Question(Base):
    __tablename__ = "questions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    flow_version_id = Column(UUID(as_uuid=True), ForeignKey("flow_versions.id"), nullable=False)
    code = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    type = Column(String, nullable=False)  # 'multiple_choice','text','number','date'
    display_order = Column(Integer, nullable=False)

class QuestionOption(Base):
    __tablename__ = "question_options"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id"), nullable=False)
    code = Column(String, nullable=False)
    text = Column(Text, nullable=False)

class FlowRule(Base):
    __tablename__ = "flow_rules"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    flow_version_id = Column(UUID(as_uuid=True), ForeignKey("flow_versions.id"), nullable=False)
    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id"), nullable=False)
    option_id = Column(UUID(as_uuid=True), ForeignKey("question_options.id"), nullable=False)
    next_question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id"), nullable=False)

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)

class UserAnswer(Base):
    __tablename__ = "user_answers"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id"), nullable=False)
    selected_option_id = Column(UUID(as_uuid=True), ForeignKey("question_options.id"), nullable=True)
    answer_text = Column(Text, nullable=True)
    answer_number = Column(Numeric, nullable=True)
    answered_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)

class UserProfileHistory(Base):
    __tablename__ = "user_profile_history"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    profile_data = Column(JSON, nullable=False)
    valid_from = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    valid_to = Column(TIMESTAMP(timezone=True), nullable=True)

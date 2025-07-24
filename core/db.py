from contextlib import contextmanager
from pathlib import Path
from sqlmodel import create_engine, Session, select, SQLModel
from .models import Entry
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///weight_mood.db")
engine = create_engine(DATABASE_URL, echo=False)

# create tables once
if not Path("weight_mood.db").exists():
    SQLModel.metadata.create_all(engine)

@contextmanager
def get_session():
    with Session(engine) as session:
        yield session

def add_entry(weight: float, mood: int):
    with get_session() as s:
        e = Entry(weight=weight, mood=mood)
        s.add(e)
        s.commit()

def get_entries():
    with get_session() as s:
        return s.exec(select(Entry).order_by(Entry.timestamp)).all()

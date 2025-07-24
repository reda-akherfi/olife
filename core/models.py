from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

# Pydantic + SQLModel hybrid
class Entry(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: datetime = Field(default_factory=datetime.utcnow, index=True)
    weight: float
    mood: int  # 1‑5

    # mnemonic: W‑M‑T (Weight‑Mood‑Timestamp)

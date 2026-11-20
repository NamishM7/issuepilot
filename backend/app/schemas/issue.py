# pydantic schema

from pydantic import BaseModel, Field, ConfigDict
from typing import Literal
from uuid import UUID
from datetime import datetime

# data received when creating an issue
class IssueCreate(BaseModel):
    title:str = Field(
        min_length=3, 
        max_length=200
    )
    body: str = Field(
        min_length=10
    )
    repository : str 
    labels : list[str] = Field(
        default_factory=list
    )

# data returned by the api
class IssueResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)   # allows pydantic to read data from sqlalchemy orm objects instead of requiring us to manually convert every record to dict
    id: UUID
    title: str
    body: str
    repository: str
    labels: list[str]
    state: Literal["open", "closed"]
    created_at: datetime

class IssueUpdate(BaseModel):

    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=200
    )

    body: str | None = Field(
        default=None,
        min_length=10
    )

    repository: str | None = None

    labels: list[str] | None = None

    state: Literal["open", "closed"] | None = None

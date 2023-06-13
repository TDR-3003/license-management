from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Users(BaseModel):
    id_user: Optional[int]
    name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    status: Optional[int]


class Login(BaseModel):
    email: str
    password: str

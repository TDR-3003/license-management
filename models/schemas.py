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


class UsersList(BaseModel):
    id_user: Optional[int]
    name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    status: Optional[int]

    def to_dict(self):
        return {
            'id_user': self.id_user,
            'name': self.name,
            'last_name': self.last_name,
            'email': self.email,
            'status': self.status
        }

    def __init__(self, id_user, name, last_name, email,status):
        super().__init__(
            id_user=id_user,
            name=name,
            last_name=last_name,
            email=email,
            status =status
        )


class Login(BaseModel):
    email: str
    password: str

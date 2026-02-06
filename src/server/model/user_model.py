from pydantic import BaseModel
from uuid import UUID


class User(BaseModel):
    uid: UUID
    nick_name: str

class UserRoom(BaseModel):
    User: User
    status: int
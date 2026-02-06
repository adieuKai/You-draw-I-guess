from uuid import UUID

from pydantic import BaseModel


class Room(BaseModel):
    rid: UUID
    room_name: str
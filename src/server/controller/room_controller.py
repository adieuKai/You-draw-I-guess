from fastapi import Form
from fastapi.routing import APIRouter

from src.server.model.room_model import Room
from src.server.service.room_service import RoomService

room_router = APIRouter()

#获取所有房间信息
@room_router.get("/list")
def get_rooms():
    """获取所有房间信息"""
    return RoomService.get_rooms()

#创建房间
@room_router.post("/create")
def create_room(room: Room):
    """创建一个房间信息"""
    return RoomService.create_room(room)

#查询房间
@room_router.get("/get/{rid}")
def get_room(rid: int):
    """查询一个房间信息"""
    return RoomService.get_room(rid)

#修改房间
@room_router.put("/update/{rid}")
def update_room(rid: int, name: str):
    """修改一个房间信息"""
    return RoomService.update_room(rid, name)

#删除房间
@room_router.delete("/delete/{rid}")
def delete_room(rid: int):
    """删除一个房间信息"""
    return RoomService.delete_room(rid)

#查看房间的用户有哪些
@room_router.get("/get_users/{rid}")
def get_room_users(rid: int):
    """查看房间的用户有哪些"""
    return RoomService.get_room_users(rid)
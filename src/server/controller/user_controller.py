from fastapi import Form
from fastapi.routing import APIRouter

from src.server.model.user_model import User
from src.server.service.user_service import UserService

user_router = APIRouter()

#创建角色
@user_router.post("/create")
def create_role(user: User):
    """创建一个角色信息"""
    return UserService.create_role(user)

#查看角色
@user_router.get("/{uid}")
def get_role(uid: int):
    """查看角色信息"""
    return UserService.get_role(uid)
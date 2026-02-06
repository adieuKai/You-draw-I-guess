from src.server.model.room_model import Room
from src.server.service.common_service import CommonService


class RoomService:
    """
    房间服务
    """

    # 获取所有房间信息
    def get_rooms(self):
        """获取所有房间信息"""
        return CommonService.http_response(code=200, message="获取所有房间信息成功", data=[])

    # 创建房间
    def create_room(self,room: Room):
        """创建一个房间信息"""
        return CommonService.http_response(code=200, message="创建房间信息成功", data=room)

    # 查询房间
    def get_room(self,rid: int):
        """查询一个房间信息"""
        return CommonService.http_response(code=200, message="查询房间信息成功", data={"rid": rid})

    # 修改房间
    def update_room(self,rid: int, name: str):
        """修改一个房间信息"""
        return CommonService.http_response(code=200, message="修改房间信息成功", data={"rid": rid, "name": name})

    # 删除房间
    def delete_room(self,rid: int):
        """删除一个房间信息"""
        return CommonService.http_response(code=200, message="删除房间信息成功", data={"rid": rid})

    # 查看房间的用户有哪些
    def get_room_users(self,rid: int):
        """查看房间的用户有哪些"""
        return CommonService.http_response(code=200, message="查看房间的用户有哪些成功", data=[])
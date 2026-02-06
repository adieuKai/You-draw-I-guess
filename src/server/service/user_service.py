from src.server.model.user_model import User
from src.server.service.common_service import CommonService


class UserService:
    # 创建角色
    def create_role(self,user: User):
        """创建一个角色信息"""
        return CommonService.http_response(code=200, message="创建角色信息成功", data=user)

    # 查看角色
    def get_role(self,uid: int):
        """查看角色信息"""
        return CommonService.http_response(code=200, message="查看角色信息成功", data={"uid": uid})
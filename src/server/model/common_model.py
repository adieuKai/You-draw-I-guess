from pydantic import BaseModel


class HttpResponse(BaseModel):
    """
    响应模型
    """
    code: int = 200
    message: str = "success"
    data: dict = {}
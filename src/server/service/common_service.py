from src.server.model.common_model import HttpResponse
from src.server.utils.logger import log

class CommonService:
    """
    通用服务类
    """
    def http_response(self,code, message, data):
        """
        封装 HTTP 响应
        """
        if code != 200:
            log.error(f"HTTP 错误: {code} {message}")
        else:
            log.info(f"HTTP 响应: {code} {message}")
        return HttpResponse(code=code, message=message, data=data)
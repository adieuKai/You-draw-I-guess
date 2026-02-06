import uvicorn
from fastapi import FastAPI

from src.server.route.router import setup_router
from src.server.utils.banner import worship
from src.server.utils.logger import setup_logging
from src.server.utils.middleware import middleware

app = FastAPI()

# 初始化日志
setup_logging()

# 显示启动横幅
worship()

# 注册路由
setup_router(app)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

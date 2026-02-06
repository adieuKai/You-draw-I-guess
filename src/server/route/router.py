#统一封装接口
from src.server.controller.room_controller import room_router
from src.server.controller.user_controller import user_router
from src.server.route.websocket import websocket_router


def setup_router(app):
    app.include_router(user_router, prefix="/user", tags=["用户接口"])
    app.include_router(room_router, prefix="/room", tags=["房间接口"])
    app.include_router(websocket_router, prefix="/ws", tags=["websocket接口"])

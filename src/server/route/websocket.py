from datetime import datetime

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query
import json
from src.server.utils.logger import log

websocket_router = APIRouter()

# 存储活动的WebSocket连接
active_connections: list[WebSocket] = []


@websocket_router.websocket("/contect")
async def websocket_endpoint(websocket: WebSocket, token: str = Query(...)):
    """WebSocket聊天端点"""
    try:
        while True:
            data = await websocket.receive_text()
            log.info(f"收到WebSocket消息: {data}")
            
            # 解析消息
            try:
                message = json.loads(data)
                # 处理消息...
                if message.get("type") == "ping":
                    message = {
                        "type": "pong",
                        "timestamp": datetime.now().timestamp()
                    }
                    await websocket.send_text(json.dumps(message))
                    continue
                # 这里可以添加自定义的消息处理逻辑
                
                # 广播消息给所有连接的客户端
                for connection in active_connections:
                    if connection != websocket:
                        await connection.send_text(data)
                        
            except json.JSONDecodeError:
                # 如果消息不是有效的JSON，直接广播
                for connection in active_connections:
                    if connection != websocket:
                        await connection.send_text(data)
                        
    except WebSocketDisconnect:
        active_connections.remove(websocket)
        log.info(f"WebSocket连接断开: {websocket.client}")
    except Exception as e:
        log.error(f"WebSocket错误: {e}")
        if websocket in active_connections:
            active_connections.remove(websocket)


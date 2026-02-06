from fastapi import Request

def middleware(app):
    @app.middleware("http")
    async def rate_limit_middleware(request: Request, call_next):
        return
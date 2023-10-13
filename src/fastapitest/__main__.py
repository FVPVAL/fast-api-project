import uvicorn

from .settings import settings

uvicorn.run(
    "fastapitest.app:api_app",
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)

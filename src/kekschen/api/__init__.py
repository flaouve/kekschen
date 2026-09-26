import threading

import uvicorn

from ..config.config import FASTAPI_HOST, FASTAPI_LOG_LEVEL, FASTAPI_PORT, FASTAPI_LOOP, FASTAPI_RELOAD

def endpoints_main() -> None:
    t = threading.Thread(
        target=server_start,
        daemon=True)
    t.start()

def server_start() -> None:
    uvicorn.run(
        "kekschen.api.endpoints:app", 
        host=FASTAPI_HOST, 
        port=FASTAPI_PORT,
        loop=FASTAPI_LOOP,
        log_level=FASTAPI_LOG_LEVEL,
        reload=FASTAPI_RELOAD
    )

if __name__ == "__main__":
    FASTAPI_RELOAD = True
    server_start()
    
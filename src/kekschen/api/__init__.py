import threading

import uvicorn

def endpoints_main() -> None:
    t = threading.Thread(
        target=server_start,
        kwargs={
            "uvicorn_reload": False
        },
        daemon=True)
    t.start()

def server_start(uvicorn_reload: bool=False) -> None:
    if not uvicorn_reload:
        uvicorn.run(
            "kekschen.api.endpoints:app", 
            host="0.0.0.0", 
            port=8000,
            loop="asyncio",
            log_level="info"
        )

    else:
        uvicorn.run(
            "kekschen.api.endpoints:app", 
            host="0.0.0.0", 
            port=8000, 
            reload=True,
            loop="asyncio"
        )

if __name__ == "__main__":
    server_start(uvicorn_reload=True)
    
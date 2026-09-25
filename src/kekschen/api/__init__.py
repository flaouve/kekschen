import threading

import uvicorn

def endpoints_main() -> None:
    t = threading.Thread(
        target=server_start,
        kwargs={
            "uvicorn_reload": False
        },
        daemon=False)
    t.start()

def server_start(uvicorn_reload=False) -> None:
    if not uvicorn_reload:
        uvicorn.run(
            "kekschen.api.endpoints:app", 
            host="127.0.0.1", 
            port=8000,
            loop="asyncio"
        )
    uvicorn.run(
        "kekschen.api.endpoints:app", 
        host="127.0.0.1", 
        port=8000, 
        reload=True,
        loop="asyncio"
    )
if __name__ == "__main__":
    server_start(uvicorn_reload=True)
    



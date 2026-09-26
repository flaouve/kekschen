import threading

import uvicorn

from ..config.env import FastAPI_Host, FastAPI_Port, FastAPI_Reload, FastAPI_Log_Level, FastAPI_Loop

def endpoints_main() -> None:
    t = threading.Thread(
        target=server_start,
        kwargs={
            "uvicorn_reload": False
        },
        daemon=True)
    t.start()

def server_start() -> None:
    uvicorn.run(
        "kekschen.api.endpoints:app", 
        host=FastAPI_Host, 
        port=FastAPI_Port,
        loop=FastAPI_Loop,
        log_level=FastAPI_Log_Level,
        reload=FastAPI_Reload
    )

if __name__ == "__main__":
    FastAPI_Reload = True
    server_start()
    
import os
from dotenv import load_dotenv


load_dotenv()

FASTAPI_HOST = str(os.getenv("FASTAPI_HOST", "0.0.0.0"))
FASTAPI_PORT = int(os.getenv("FASTAPI_PORT", 8080))
FASTAPI_RELOAD: bool = str(os.getenv("FASTAPI_RELOAD", False)).lower() in ("true", "1", "yes")
FASTAPI_LOG_LEVEL = str(os.getenv("FASTAPI_LOG_LEVEL", "info"))
FASTAPI_LOOP = str(os.getenv("FASTAPI_LOOP", "asyncio"))

def type_control():
    print("Environment Var~ Loaded From .env file Or Session Env. \n",
          f"FastApi_Host={type(FASTAPI_HOST), FASTAPI_HOST}\n",
          f"FastApi_Port={type(FASTAPI_PORT) , FASTAPI_PORT}\n",
          f"FastApi_Reload={type(FASTAPI_RELOAD), (FASTAPI_RELOAD)}\n",
          f"FastApi_Log_Level={type(FASTAPI_LOG_LEVEL), (FASTAPI_LOG_LEVEL)}\n",
          f"FastApi_Loop={type(FASTAPI_LOOP), (FASTAPI_LOOP)}\n")

if __name__ == "__main__":
    type_control()

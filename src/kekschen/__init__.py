def main() -> None:
    from .main import main
    main()

def api() -> None:
    from .api.__init__ import server_start
    server_start()

def db() -> None:
    from .database.__init__ import main
    main()

def core() -> None:
    from .core.__init__ import main
    main()

def config() -> None:
    from .config.config import type_control
    type_control()
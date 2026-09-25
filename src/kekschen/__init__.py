def main() -> None:
    from .main import main
    main()

def api() -> None:
    from .api.__init__ import server_start
    server_start()

def db() -> None:
    from .db.__init__ import main
    main()

def mechanic() -> None:
    from .mechanic.__init__ import main
    main()
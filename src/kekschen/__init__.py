def main() -> None:
    from .main import main
    main()

def api() -> None:
    from .api.__init__ import server_start
    server_start()

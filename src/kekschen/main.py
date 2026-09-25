import threading

from .api.__init__ import endpoints_main

def main() -> None:
    t = threading.Thread(target=endpoints_main, daemon=False)
    t.start()
    print("Hello from kekschen!")

def api() -> None:
    t = threading.Thread(target=endpoints_main, daemon=False)
    t.start()

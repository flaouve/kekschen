import asyncio

def main():
    print("Hello from kekschen!")

async def api():
    from .api.__init__ import main
    await main()
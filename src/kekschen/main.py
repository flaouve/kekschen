import threading

from .api.__init__ import endpoints_main

api_thread = None

def main() -> None:
    menu()

def menu():
    while True:
        print("1. Start API")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1" or choice.lower() == "start api" or choice.lower() == "api" or choice.lower() == "start":
            api()
        elif choice == "2" or choice.lower() == "exit" or choice.lower() == "quit" or choice.lower() == "close" or choice.lower() == "stop" or choice.lower() == "end":
            break
        else:
            print("Invalid choice. Please try again.")

def api() -> None:
    global api_thread
    if api_thread and api_thread.is_alive():
        print("API is already running.")
        return
    print("Starting API...")
    api_thread = threading.Thread(
        target=endpoints_main,
        daemon=True
    )
    api_thread.start()

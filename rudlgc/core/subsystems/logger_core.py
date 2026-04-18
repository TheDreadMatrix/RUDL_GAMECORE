from datetime import datetime

def _callOnce(error_message):
    def decorator(func):
        called = False

        def wrapper(*args, **kwargs):
            nonlocal called

            if called:
                now = datetime.now().strftime("%H:%M:%S")
                print(f"\033[91m[{now}]-[ERROR]: {error_message}\033[0m")
                print(f"\033[91m[{now}]-[ERROR]: Game failure exit\033[0m")
                exit(1)

            called = True
            return func(*args, **kwargs)

        return wrapper
    return decorator



class Logger:
    COLORS = {
        "INFO": "\033[94m", 
        "WARNING": "\033[33m",
        "MAGENTA-USER": "\033[35m",
        "TRACE-USER": "\033[92m",
        "ERROR": "\033[91m",
        "RESET": "\033[0m"
    }
        
    @staticmethod
    def trace(message, as_error=False):
        now = datetime.now().strftime("%H:%M:%S")
        color = Logger.COLORS["TRACE-USER"] if not as_error else Logger.COLORS["ERROR"]
        reset = Logger.COLORS["RESET"]
        print(f"{color}[{now}]-[TRACE-USER]: {message}{reset}")

    @staticmethod
    def traceMagenta(message):
        now = datetime.now().strftime("%H:%M:%S")
        color = Logger.COLORS["MAGENTA-USER"]
        reset = Logger.COLORS["RESET"]
        print(f"{color}[{now}]-[TRACE-USER]: {message}{reset}")

    @staticmethod
    def _system_log(tag, message):
        now = datetime.now().strftime("%H:%M:%S")
        color = Logger.COLORS.get(tag, "")
        reset = Logger.COLORS["RESET"]
        print(f"{color}[{now}]-[{tag}]: {message}{reset}")
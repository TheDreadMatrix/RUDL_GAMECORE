from datetime import datetime





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
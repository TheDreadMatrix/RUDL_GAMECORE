from datetime import datetime





class Logger:
    __COLORS = {
        "INFO": "\033[94m", 
        "SUCCESS": "\033[34m",
        "WARNING": "\033[33m",
        "RESOURCE": "\033[36m",
        "SCENE": "\033[35m",
        "USER": "\033[92m",
        "ERROR": "\033[91m",
    }
        
    
    def trace(self, message):
        self._system_log("USER", message)


    @staticmethod
    def _system_log(tag, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        color = Logger.__COLORS.get(tag, "\033[40m")

        if tag not in Logger.__COLORS: 
            tag = "UNDEFINED"

        print(f"{color}({now})-[{tag}]: {message}\033[0m")
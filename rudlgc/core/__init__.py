import platform
from datetime import datetime
import os


def _callOnce(error_message="It is strictly forbidden to call private functions and methods."):
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


def _getOs():
    system = platform.system().lower()
    machine = platform.machine().lower()
    name_os = ""

    if system == "windows":
        name_os = "Windows"
    
    if system == "darwin":
        if "iphone" in machine or "ipad" in machine:
            name_os = "iOS"
        name_os = "macOS"

    if system == "linux":
        if ("ANDROID_ROOT" in os.environ or "ANDROID_DATA" in os.environ or "ANDROID_BOOTLOGO" in os.environ):
            name_os = "Android"
        name_os =  "Linux"

    return name_os.upper()
import json

def load_config(path):
    with open(path, 'r') as file:
        return json.load(file)
    
def send_command(device_api, command):
    # Placeholder for sending a command to a device
    print(f"Sending command {command} to device {device_api}")
    # Implement actual command sending logic here

class HomeBridge(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(HomeBridge, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

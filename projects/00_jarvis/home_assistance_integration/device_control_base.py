import requests
import json
from common import load_config, HomeBridge

home_bridge_config = load_config("./configs/homebridge.json")
lamp_config = load_config("./configs/lamp.json")
# HomeBridge server details
HOMEBRIDGE_IP = home_bridge_config["ip"]  # Replace with your HomeBridge server IP
HOMEBRIDGE_PORT = home_bridge_config["port"]  # Replace with your HomeBridge server port
HOMEBRIDGE_TOKEN = home_bridge_config["token"]  # Replace with your HomeBridge API token

# Lamp accessory ID (you can find this in the HomeBridge UI)
LAMP_ACCESSORY_ID = lamp_config["desktop_lamp_id"]

# HomeBridge API endpoint
url = f'http://{HOMEBRIDGE_IP}:{HOMEBRIDGE_PORT}/api/accessories/{LAMP_ACCESSORY_ID}'

# Headers for the request



class DeviceControlBase(metaclass=HomeBridge):
    def __init__(self, device_id = 0):
        self.device_id = device_id
        self.headers = {
        'Authorization': f'Bearer {HOMEBRIDGE_TOKEN}',
        'Content-Type': 'application/json'
        }
    
    def set_status(status):
        """Set the lamp status (on/off)."""
        data = {
            'characteristicType': 'On',
            'value': status
        }
        
        response = requests.put(url, headers=self.headers, data=json.dumps(data))
        
        if response.status_code == 200:
            print(f"Lamp turned {'on' if status else 'off'} successfully.")
        else:
            print(f"Failed to set lamp status. Status code: {response.status_code}")

    def get_status():
        """Get the current status of the lamp."""
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            lamp_data = response.json()
            lamp_status = lamp_data['characteristics']['On']
            print(f"Lamp is currently {'on' if lamp_status else 'off'}.")
        else:
            print(f"Failed to get lamp status. Status code: {response.status_code}")

# Example usage
if __name__ == "__main__":

    device = DeviceControlBase()
    # Turn the lamp on
    device.set_status(True)
    
    # Get the current status of the lamp
    device.get_status()
    
    # Turn the lamp off
    device.set_status(False)
    
    # Get the current status of the lamp
    device.get_status()
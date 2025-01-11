from .function_call import get_location_based_on_ip, get_weather

__all__ = ["get_location_based_on_ip", "get_weather"]

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_location_based_on_ip",
            "description": "Get the location based on the user's IP address",
            "parameters": {
                "type": "object",
                "properties": {}
            },
    }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of an location, the user shoud supply a location first",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                }
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_location_based_on_ip",
            "description": "Get the location based on the user's IP address",
            "parameters": {
                "type": "object",
                "properties": {}
            },
        }
    },
]

functions = {
    "get_weather": get_weather,
    "get_location_based_on_ip": get_location_based_on_ip,
}


def process_tool_calls(tool):
    if tool.function.name in functions.keys():
        if tool.function.arguments is not None:
            response = functions[tool.function.name](**eval(tool.function.arguments))
        else:
            response = functions[tool.function.name]()
        return response
    else:
        return None

def process_response(message, messages):
    if message.tool_calls is not None:
        tool = message.tool_calls[0]
        response = process_tool_calls(tool)
        messages.append(message)
        messages.append({"role": "tool", "tool_call_id": tool.id, "content": "{}".format(str(response))})
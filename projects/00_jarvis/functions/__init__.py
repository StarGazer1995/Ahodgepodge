from .function_call import get_location_based_on_ip, get_weather, get_search_results

__all__ = ["get_location_based_on_ip", "get_weather", "get_search_results"]

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
            "description": "Get weather of a location, the user should supply a location first",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["location"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_search_results",
            "description": "Retrieve search results for a given keyword using the Google Custom Search API",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "The search term or phrase to query",
                    }
                },
                "required": ["keyword"]
            },
        }
    }
]

functions = {
    "get_weather": get_weather,
    "get_location_based_on_ip": get_location_based_on_ip,
    "get_search_results": get_search_results,
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
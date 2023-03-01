from pprint import pprint
from typing import  Literal,  Union
import requests
from decorators import handle_exception

data_format = Literal["json", "text"]

@handle_exception
def get_data(url: str, format: data_format = "json") -> Union[list, str]:
    response = requests.get(url)
    data = {"text": response.text, "json": response.json()}
    return data[format]




if __name__ == "__main__":
    pprint(get_data("https://jsonplaceholder.typicode.com/posts"))


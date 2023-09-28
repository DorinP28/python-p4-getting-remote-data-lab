import requests
import json


class GetRequester:
    def __init__(self, url: str):
        self.url = url

    def get_response_body(self) -> str:
        response = requests.get(self.url)
        return response.content

    def load_json(self) -> dict:
        return json.loads(self.get_response_body())


if __name__ == "__main__":
    instance = GetRequester(
        "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    )
    print(instance.load_json())

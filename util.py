import requests

class Util:
    def __init__(self) -> None:
        pass

    def getResponse(self, endpoint: str = "api/")->dict[str, str]|requests.RequestException:
        try:
            response: requests.Response = requests.get(f"https://api-pomodoroplanner.vercel.app/{endpoint}")
            return response.json()
        except requests.RequestException as e:
            return e
import requests

def get_weather():
    url = "https://wttr.in"
    try:
        response = requests.get(url)
        response.raise_for_status()

        print(f"Погода сегодня: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе погоды: {e}")


if __name__ == "__main__":
    get_weather()
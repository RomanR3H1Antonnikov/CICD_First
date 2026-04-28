import requests

def get_weather(city=""):
    url = f"https://wttr.in/{city}?m"

    try:
        response = requests.get(url)
        response.raise_for_status()

        print(f"Погода сегодня в {city if city else "вашем городе"}: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе погоды: {e}")


if __name__ == "__main__":
    print("""Добрый день! Готовы узнать прогноз погоды? Доступные команды:
    1. Нажмите Enter - погода для вашего местоположения
    2. Введите название города - погода для указанного города
    3. Введите 'exit' - выход из программы""")

    while True:
        city = input("Введите город (или нажмите Enter): ").strip()

        if city.lower() == 'exit':
            print("Хорошего дня!")
            break
        elif city:
            get_weather(city)
        else:
            get_weather()

        print()
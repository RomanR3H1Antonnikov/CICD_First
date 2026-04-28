import requests

def get_weather(city=None):
    if city:
        url = f"https://wttr.in/{city}?m"
    else:
        url = "https://wttr.in/?m"

    try:
        response = requests.get(url)
        response.raise_for_status()

        print(f"Погода сегодня в {city if city else "вашем городе"}: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе погоды: {e}")


if __name__ == "__main__":
    print("Добрый день! Готовы узнать прогноз погоды? Доступные команды:")
    print()
    print("1. Нажмите Enter - погода для вашего местоположения")
    print("2. Введите название города - погода для указанного города")
    print("3. Введите 'exit' - выход из программы")
    print()

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
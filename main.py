import requests

country = input("Введіть назву країни: ")
url = f"https://restcountries.com/v3.1/name/{country}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()[0]
    print(f"Назва: {data['name']['common']}")
    print(f"Столиця: {data['capital'][0]}")
    print(f"Населення: {data['population']}")
    print(f"Площа: {data['area']} км²")
    print(f"Прапор: {data['flags']['png']}")
else:
    print("Країна не знайдена!")

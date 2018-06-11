import requests

def get_weather(url):
    result=requests.get(url)
    if result.status_code==200:
        return result.json()
    else:
        print("Ошибка")

if __name__=="__main__":
    data = get_weather('http://api.openweathermap.org/data/2.5/weather?id=498817&units=metric&appid=e200eeccd52d6bcf86e203ef78a20d75')
    print(data)

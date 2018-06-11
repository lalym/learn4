import requests

def get_names(url):
    result=requests.get(url)
    if result.status_code==200:
        return result.json()
    else:
        print("Ошибка")

if __name__=="__main__":
    data = get_names('http://apidata.mos.ru/v1/datasets/2009/rows?api_key=c8ca730b3f3e7202bf20f00710d254e8')
    print(data)

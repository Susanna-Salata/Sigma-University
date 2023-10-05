from requests import Session
from bs4 import BeautifulSoup


def scraping():

    url9='https://www.gismeteo.ua/ua/weather-kyiv-4944/now/'
    url10='https://www.gismeteo.ua/ua/weather-washington-7150/now/'
    url11='https://www.gismeteo.ua/ua/weather-london-744/now/'


    weather = {}

    # фейковий заголовок для захисту від ботів
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    # сесія для куків
    work = Session()


    def get_data_web9(url):
        pass
        response = work.get(url, headers=headers)
        # print("Status: Gismeteo Kyiv", response.status_code)
        if response.status_code == 200:
            response.encoding = 'utf8'
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            datas = soup.find('div', class_="day-0")
            status = datas.find('a', class_="tooltip").get("data-text")
            temp = datas.find('span', class_="unit unit_temperature_c").text
            weather['gis1'] = 'Погода в Києві - ' + status + ' ' + temp
        else:
            weather['gis1'] = 'Погода в Києві - сервер тимчасово не відповідає'

    def get_data_web10(url):
        pass
        response = work.get(url, headers=headers)
        # print("Status: Gismeteo Washington", response.status_code)
        if response.status_code == 200:
            response.encoding = 'utf8'
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            datas = soup.find('div', class_="day-0")
            status = datas.find('a', class_="tooltip").get("data-text")
            temp = datas.find('span', class_="unit unit_temperature_c").text
            weather['gis2'] = 'Погода в Вашингтоні - ' + status + ' ' + temp
        else:
            weather['gis2'] = 'Погода в Вашингтоні - сервер тимчасово не відповідає'


    def get_data_web11(url):
        pass
        response = work.get(url, headers=headers)
        # print("Status: Gismeteo London", response.status_code)
        if response.status_code == 200:
            response.encoding = 'utf8'
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            datas = soup.find('div', class_="day-0")
            status = datas.find('a', class_="tooltip").get("data-text")
            temp = datas.find('span', class_="unit unit_temperature_c").text
            weather['gis3'] = 'Погода в Лондоні - ' + status + ' ' + temp
        else:
            weather['gis3'] = 'Погода в Лондоні - сервер тимчасово не відповідає'


    try:
        get_data_web9(url9)
    except: pass
    try:
        get_data_web10(url10)
    except: pass
    try:
        get_data_web11(url11)
    except: pass

    return weather


if __name__=="__main__":
    w = scraping()

    print(w)
from flask import Flask, abort, request
from weather import get_weather
from datetime import datetime
from news_list import all_news
from mosnames import get_names

city_id = 498817
apikey = 'e200eeccd52d6bcf86e203ef78a20d75'

app=Flask(__name__)

@app.route("/")
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?id=%s&units=metric&appid=%s' % (city_id, apikey)
    weather_f = get_weather(url)
    cur_date = datetime.now().strftime('%d.%m.%Y')
    result = "<p> <b> Температура:</b> %s </p>" % weather_f['main']['temp']
    result+= "<p> <b>  Город:</b> %s</p>" % weather_f['name']
    result+= "<p> <b>  Дата:</b> %s</p>" % cur_date
    return result

@app.route("/names")
def names():
    url = 'http://apidata.mos.ru/v1/datasets/2009/rows?api_key=c8ca730b3f3e7202bf20f00710d254e8'
    names_data = get_names(url)
    result = '''<table> 
        <tr>
            <th>Имя:</th>
            <th>Год:</th>
            <th>Месяц:</th>
            <th>Кол-во человек:</th>
        </tr>'''


    for n in names_data:
        result += '''<tr>
                   <td>{}</td>
                   <td>{}</td>
                   <td>{}</td>
                   <td>{}</td>
                </tr>'''.format(n['Cells']['Name'], n['Cells']['Year'], n['Cells']['Month'],
                                n['Cells']['NumberOfPersons'])

        result += '</table>'
        return result


@app.route("/names/<int:year_id>")
def year_by_id(year_id):
    url = "http://apidata.mos.ru/v1/datasets/2009/rows?api_key=c8ca730b3f3e7202bf20f00710d254e8"
    name = get_names(url)
    year_to_show = [years for years in name if years['Cells']['Year'] == year_id]

    result = '''<table>
    <tr>
        <th>Имя:</th>
        <th>Год:</th>
        <th>Месяц:</th>
        <th>Кол-во человек:/th>'''

    for n in year_to_show:
        result += '''<tr>
           <td>{}</td>
           <td>{}</td>
           <td>{}</td>
           <td>{}</td>
        </tr>'''.format(n['Cells']['Name'], n['Cells']['Year'], n['Cells']['Month'], n['Cells']['NumberOfPersons'])

    result += '</table>'
    return result


@app.route("/news")
def all_the_news():
    colors = ['green', 'blue', 'red']
    try:
        limit = int(request.args.get('limit', 0))
    except:
        limit = 10
    color = request.args.get('color', 'black') if request.args.get('color') in colors else 'black'
    return '<h1 style ="color: %s" >News: <small> %s </small> </h1>' % (color, limit)



@app.route("/news/<int:news_id>")
def news_by_id(news_id):
    news_to_show = [news for news in all_news if news['id'] == news_id]
    if len(news_to_show) == 1:
        result = "<h1>%(title)s</h1><p><i>%(date)s</i><p>%(text)s</p>"
        result = result % news_to_show[0]
        return result
    else:
        abort(404)


if __name__=="__main__":
    app.run(port=5000, debug=True)



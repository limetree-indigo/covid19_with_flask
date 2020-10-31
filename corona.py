import requests, xmltodict, json
from datetime import date, timedelta

def get_city_data():
    today = date.today()
    yesterday = today - timedelta(days=1)

    today = today.strftime("%Y%m%d")
    yesterday = yesterday.strftime("%Y%m%d")


    url= "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"
    params ={
        'serviceKey':'/RiLDbQOrX1DYkcfCT5/LyQYEKJ3G4If9ktXL8/B8o3aCQfi/S6D0g+OFjWQD+dZa2ru1Iwbasb9TV+IlJU0wA==',
        'pageNo': '1',
        'numOfRows': '30',
        'startCreateDt' : yesterday,
        'endCreateDt': today,
    }

    res = requests.get(url, params=params)
    # print(res.text)

    dict_data = xmltodict.parse(res.text)
    json_data = json.dumps(dict_data)
    dict_data = json.loads(json_data)
    # pprint(dict_data)

    items = dict_data['response']['body']['items']['item']

    f_string = date.today().strftime("%Y-%m-%d")

    results = []
    if f_string in items[0]['createDt']:
        for item in items:
            if f_string in item['createDt']:
                results.append(item)
    else:
        results = items
    results.reverse()
    # print(results)
    return results

if __name__ == "__main__":
    print(get_city_data())
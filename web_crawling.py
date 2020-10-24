import requests
from bs4 import BeautifulSoup

# 코로나 요약 현황을 가져오는 함수
def get_corona_summary():
    url = "http://ncov.mohw.go.kr/"
    res = requests.get(url)

    soup = BeautifulSoup(res.text,'lxml')
    # print(soup)

    # 확진환자/완치/치료중/사망 수 가져오기
    peoples = soup.select('.liveNumOuter ul.liveNum .num')
    # print(peoples)

    # 데이터 정리
    results={
        '확진환자' : int(peoples[0].text.replace(',','').replace('(누적)','')),
        '완치' : int(peoples[1].text.replace(',','')),
        '치료중' : int(peoples[2].text.replace(',','')),
        '사망' : int(peoples[3].text.replace(',',''))
    }
    # print(results)
    return results


# 테스트 용 코드
if __name__ == "__main__":
    print(get_corona_summary())
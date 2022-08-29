"""
Uncatched Bugs:
현재 예기치 못한 오류로 마지막 날의 급식 정보가 제공되지 않음
"""

from bs4 import BeautifulSoup as bs
import bs4
import requests

def parse_menu():
    url = 'http://school.gyo6.net/yn36ms/070501/food'
    try:
        page = requests.get(url)
    except Exception as e:
        print("예기치 않은 문제가 발생했습니다.\n발생 유형:", e)
    else:
        soup = bs(page.text, 'html.parser')

        this_month = soup.select('.diet_box')
        day = [["breakfast"], ["lunch"], ["dinner"]]
        menu = []
        i = 0
        for meal in this_month:
            if i % 3 == 0: menu.append(day); day = [[], [], []]
            a = meal.select_one('.menu').contents
            for j in a:
                if type(j) == bs4.element.NavigableString : day[i%3].append(j)
            i += 1
        return {"data": menu} # js 단계에서 처리하기 위해 dictionary <=> Object 형태로 반환

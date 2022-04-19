"""
현재 예기치 못한 오류로 마지막 날의 급식 정보가 제공되지 않고 있습니다.
"""

import requests
from bs4 import BeautifulSoup as bs
import bs4
import json
import datetime


try:
    page = requests.get('http://school.gyo6.net/yn36ms/070501/food')
except Exception as e:
    print("예기치 않은 문제가 발생했습니다.\n발생 유형:", e)
else:
    soup = bs(page.text, 'html.parser')


    this_month = soup.select('.diet_box')
    day = [[], [], []]
    menu = []
    i = 0
    for meal in this_month:
        if i % 3 == 0: menu.append(day); day = [i//3+1, [], [], []]
        a = meal.select_one('.menu').contents
        for j in a:
            if type(j) == bs4.element.NavigableString : day[i%3+1].append(j)
        i += 1
    with open('c:/projects/lunch/menu.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(menu, indent=2, ensure_ascii=False))

    #debub method
    """
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(menu[20])
    """


    # printing method
    now = datetime.datetime.now()
    print(f'오늘({now.month}월 {now.day}일)의 급식 정보')
    today_diet = menu[now.day]
    print('💗 아침 💗')
    for _ in today_diet[1]:
        print(_)
    print('💗 점심 💗')
    for _ in today_diet[2]:
        print(_)
    print('💗 저녁 💗')
    for _ in today_diet[3]:
        print(_)

    # print(soup.select_one('.diet_tb'))

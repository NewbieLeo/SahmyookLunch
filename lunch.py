"""
현재 예기치 못한 오류로 마지막 날의 급식 정보가 제공되지 않고 있습니다.
"""

from bs4 import BeautifulSoup as bs
from tkinter import *
import os
import bs4
import json
import datetime
from pyparsing import col
import requests



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
    with open(os.path.dirname(__file__) + '/menu.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(menu, indent=2, ensure_ascii=False))

    #debug method
    """
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(menu[20])
    """


    # printing method
    now = datetime.datetime.now()
    print(f'오늘({now.month}월 {now.day}일)의 급식 정보')
    today_diet = menu[now.day]
    print('\n💗 아침 💗')
    for _ in today_diet[1]:
        print(_)
    print('\n💗 점심 💗')
    for _ in today_diet[2]:
        print(_)
    print('\n💗 저녁 💗')
    for _ in today_diet[3]:
        print(_)

    # gui method
    root = Tk()
    root.title('오늘의 급식')
    label = Label(root, text=f'{now.month}월 {now.day}일', font=('나눔스퀘어', 20))
    label.grid(column=1, row=0)
    breakfast = Listbox(root, height=0, selectmode='extended', font='나눔스퀘어')
    for i in today_diet[1]:
        breakfast.insert(END, i)
    lunch = Listbox(root, height=0, selectmode='extended', font='나눔스퀘어')
    for i in today_diet[2]:
        lunch.insert(END, i)
    dinner = Listbox(root, height=0, selectmode='extended', font='나눔스퀘어')
    for i in today_diet[3]:
        dinner.insert(END, i)
    Label(text='아침', font=('나눔스퀘어',14)).grid(column=0, row=1)
    breakfast.grid(column=0, row=2)
    Label(text='점심', font=('나눔스퀘어',14)).grid(column=1, row=1)
    lunch.grid(column=1, row=2)
    Label(text='저녁', font=('나눔스퀘어',14)).grid(column=2, row=1)
    dinner.grid(column=2, row=2)
    root.mainloop()

    # print(soup.select_one('.diet_tb'))

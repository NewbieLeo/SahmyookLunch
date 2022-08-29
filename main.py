import lunch
import os
import json
import webbrowser as wb

menu = lunch.parse_menu() # motherf*cking gbe
with open(os.path.dirname(__file__) + '/menu.json', 'w', encoding='utf-8') as file:
    file.write('data = ' + json.dumps(menu, indent=2, ensure_ascii=False))
wb.open("file://" + os.path.realpath("index.html"))
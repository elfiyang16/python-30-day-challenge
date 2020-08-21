import requests
import datetime
from requests_html import HTML

now = datetime.datetime.now()
year = now.year

url = "https://www.boxofficemojo.com/year/world/"


def url_to_txt(url, filename="word.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"word-{year}.html", "w") as f:
                f.write(html_text)
        return html_text
    return ""


html_text = url_to_txt(url)
r_html = HTML(html=html_text)
table_class = ".imdb-scroll-table"
# like jquery in a way
r_table = r_html.find(table_class)

# print(r_table)
if len(r_table) == 1:
    print(r_table[0].text)
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header = rows[0]
    for row in rows[1:]:
        print(row.text)

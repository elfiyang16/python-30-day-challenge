import requests
import datetime
from requests_html import HTML
import pandas as pd
import os
import sys

BASE_DIR = os.path.dirname(__file__)


def url_to_txt(url, filename="word.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        # save html to a file
        if save:
            with open(f"word-{year}.html", "w") as f:
                f.write(html_text)
        return html_text
    return None


def parse_and_extract(url, name="2020"):
    html_text = url_to_txt(url)
    # just incase we can't get the document, just return
    if html_text == None:
        return False
    # save html to variable
    r_html = HTML(html=html_text)
    table_class = ".imdb-scroll-table"
    # like jquery in a way
    r_table = r_html.find(table_class)

    # if we find such element
    if len(r_table) == 0:
        return False

    # select the first element
    parsed_table = r_table[0]
    # get all the trs
    rows = parsed_table.find("tr")
    # the first row is the header
    header_row = rows[0]
    header_cols = header_row.find("th")
    # iterate through header th to find the column names
    header_names = [x.text for x in header_cols]
    # a holder for tables
    table_data = []
    # get all data from each row
    for row in rows[1:]:
        cols = row.find("td")
        row_data = []
        # row_dict_data = {}
        # iterable
        for i, col in enumerate(cols):
            header_name = header_names[i]
            # %,Foreign,% problem with the header thou
            # row_dict_data[header_name]= col.text
            row_data.append(col.text)
        table_data.append(row_data)
    # print(header_names)
    # print(table_data)
    # ['Rank', 'Release Group', 'Worldwide', 'Domestic', '%', 'Foreign', '%']
    # [['1', 'Bad Boys for Life', '$424,617,855', '$204,417,855', '48.1%', '$220,200,000', '51.9%'],
    # get it store in file dynamically
    path = os.path.join(BASE_DIR, "data")
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join("data", f"{name}.csv")

    df = pd.DataFrame(table_data, columns=header_names)
    df.to_csv(filepath, index=False)
    return True


def run(start_year=None, years_ago=1):
    if start_year == None:
        now = datetime.datetime.now()
        start_year = now.year
    # assertation
    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert len(f"{start_year}") == 4
    #  interate through start to ago years and scrape through
    for i in range(0, years_ago+1):
        url = f"https://www.boxofficemojo.com/year/world/{start_year}/"
        finished = parse_and_extract(url, name=start_year)
        if finished:
            print(f"Finished{start_year}")
        else:
            print(f"{start_year} not finished ")
        start_year -= 1


if __name__ == "__main__":
    #  pass in sys arg as input :
    # python3 -i scrape.py 2015 5
    #  if input is mal formated then pass in default input
    try:
        start = int(sys.argv[1])
    except:
        start = None
    try:
        count = int(sys.argv[2])
    except:
        count = 1
    run(start_year=start, years_ago=count)

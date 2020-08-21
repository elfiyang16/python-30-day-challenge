import requests
import datetime
from requests_html import HTML
import pandas as pd

now = datetime.datetime.now()
year = now.year

url = "https://www.boxofficemojo.com/year/world/"


def url_to_txt(url, filename="word.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        # save html to a file
        if save:
            with open(f"word-{year}.html", "w") as f:
                f.write(html_text)
        return html_text
    return ""


def parse_and_extract(url, name="2020"):
    html_text = url_to_txt(url)
    # save html to variable
    r_html = HTML(html=html_text)
    table_class = ".imdb-scroll-table"
    # like jquery in a way
    r_table = r_html.find(table_class)

    # if we find such element
    if len(r_table) == 1:
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
            # iterable
            for i, col in enumerate(cols):
                row_data.append(col.text)
            table_data.append(row_data)
        # print(header_names)
        # print(table_data)
    # ['Rank', 'Release Group', 'Worldwide', 'Domestic', '%', 'Foreign', '%']
    # [['1', 'Bad Boys for Life', '$424,617,855', '$204,417,855', '48.1%', '$220,200,000', '51.9%'],
    df = pd.DataFrame(table_data, columns=header_names)
    df.to_csv(f"data/{name}.csv", index=False)

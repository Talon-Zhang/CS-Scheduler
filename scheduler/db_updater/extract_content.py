#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup


def extract_content(html):
    print("Start extracting contents:")
    headers = list()
    infos = list()
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find_all(attrs={"class": "datadisplaytable"})
    try:
        rows = table[0].find_all("tr")
        for row in rows:
            try:
                if row.th["class"][0] == "ddheader":
                    for col in row.find_all("th"):
                        if col.string is not None:
                            headers.append(col.string)
                        else:
                            headers.append("Date")
            except TypeError:
                one_row = list()
                if row.td["class"][0] == "dddefault":
                    cols = row.find_all("td")
                    for col in cols:
                        if col.get_text() == "\n\nadd to worksheet\n\n":
                            one_row.append("open")
                        elif col.get_text() == "C":
                            one_row.append("close")
                        elif col.get_text() == "\xa0":
                            one_row.append(None)
                        else:
                            one_row.append(col.get_text())
                    infos.append(one_row)
    except IndexError:
        pass
    print("These are the headers:")
    print(headers)
    print("These are the contents:")
    print(infos[1])
    return infos
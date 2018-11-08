# https://votesmart.org/candidate/key-votes/65443/tim-walz#.W-OqxdVKjIU

import sqlite3 as sq
import requests as urlr
from bs4 import BeautifulSoup as bs
from datetime import date, timedelta

class scraper():
    dates = {"Jan.":1, "Feb.":2, "March":3, "April":4, "May":5, "June":6, "July":7, "Aug":8, "Sept.":9, "Oct.":10, "Nov.":11, "Dec.":12}
    def __init__(self):
        self.url = 'https://votesmart.org/candidate/key-votes/65443/tim-walz#.W-OqxdVKjIU'
        self.today = date.today()
        self.getPage()
        self.parse(self.soup)

    def getPage(self):
        page = urlr.get(self.url)
        self.soup = bs(page.content, 'html.parser')

    def parse(self, soup):
        for i, div in enumerate(soup.findAll("div", {"class", "border-top-1"})):
            for j, tr in enumerate(div.findAll("tr")):
                table = []
                for td in tr.findAll("td"):
                    table.append(td.getText())
                if table == []:
                    continue
                vote_date = table[0].split(" ")
                vote_date = date(int(vote_date[2]), self.dates[vote_date[0]], int(vote_date[1][:-1]))
                if vote_date >= self.today - timedelta(60):
                    print("{}\n\t{}\n\t{} - {}".format(vote_date, tale[2], table[4], table[3]))

                else:
                    break
a = scraper()

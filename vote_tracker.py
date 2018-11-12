# https://votesmart.org/candidate/key-votes/65443/tim-walz#.W-OqxdVKjIU

import sqlite3 as sq
import requests as urlr
from bs4 import BeautifulSoup as bs
from datetime import date, timedelta

class scraper():
    # months on votesmart votes are formatted as a strings
    dates = {"Jan.":1, "Feb.":2, "March":3, "April":4, "May":5, "June":6, "July":7, "Aug":8, "Sept.":9, "Oct.":10, "Nov.":11, "Dec.":12}

    def __init__(self):
        #self.url = 'https://votesmart.org/candidate/key-votes/65443'#/tim-walz#.W-OqxdVKjIU'
        self.url2 = 'https://votesmart.org/officials/NA/C/-congressional'
        self.today = date.today()
        self.getCandidates()
        self.parseCandidates(self.candidate_soup)
        self.getPage()
        self.parse(self.soup)

    def getCandidates(self):
        page = urlr.get(self.url2)
        self.candidate_soup = bs(page.content, 'html.parser')

    def parseCandidates(self, soup):
        for div in soup.findAll("div", {"class", "span-3"}):
            for a in div.findAll("a"):
                item = a.get('href')
                pieces = item.upper().split("/")
                names = pieces[3].split("-")
                if names[0] == "TIM" and names[1] == "WALZ":
                    self.url = 'https://votesmart.org/candidate/key-votes/{}'.format(pieces[2])

    def getPage(self):
        page = urlr.get(self.url)
        self.soup = bs(page.content, 'html.parser')

    def parse(self, soup):
        for div in soup.findAll("div", {"class", "border-top-1"}):
            for tr in div.findAll("tr"):
                ''' Steps through the rows in the table (tr) and grabs the data from each clumn (td)
                Appends the data to the list 'table'. If the list is empty it goes to the next row
                Otherwise checks the date and if the date is more than 60 days ago breaks the loop.
                Prints out the vote with the date, vote discription, candidates vote, outcome
                '''
                table = []
                for td in tr.findAll("td"):
                    table.append(td.getText())
                if table == []:
                    continue
                vote_date = table[0].split(" ")
                vote_date = date(int(vote_date[2]), self.dates[vote_date[0]], int(vote_date[1][:-1]))
                if vote_date >= self.today - timedelta(60):
                    print("{}\n\t{}\n\t{} - {}".format(vote_date, table[2], table[4], table[3]))
                else:
                    break
a = scraper()

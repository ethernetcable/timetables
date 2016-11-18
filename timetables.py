from bs4 import BeautifulSoup
from urllib import request
from string import ascii_letters, digits
from time import sleep
from os import system

def nonindent(string):
    for i in string:
        if i in ascii_letters or i in digits:
            return string[string.index(i):]
            break

def departures(station):
    while True:
        url = 'http://ojp.nationalrail.co.uk/service/ldbboard/dep/' + station
        soup = BeautifulSoup(request.urlopen(url), 'html.parser')
        
        dest = soup('td', class_='destination')[0]
        dest = nonindent(dest.get_text())[:-1]

        sch = soup('td', class_='status')[0]
        sch = nonindent(sch.get_text())

        status = soup('td', 'status')[1]
        status = status.get_text()
        if 'late' in status:
            status = 'Due ' + status[:5]
        elif 'early' in status:
            status = 'Due ' + status[:5]
        else:
            status = 'On time'

        platform = soup.tbody('td')[3]
        platform = platform.get_text()

        system('clear')
        print('-' * 20)
        print('Next departure from ' + station)
        print('-' * 20)
        print('Destination: ' + dest)
        print('Scheduled:   ' + sch)
        print('Status:      ' + status)
        print('Platform:    ' + platform)
        print('-' * 20)
        
        sleep(1)

def arrivals(station):
    while True:        
        url = 'http://ojp.nationalrail.co.uk/service/ldbboard/arr/' + station
        soup = BeautifulSoup(request.urlopen(url), 'html.parser')

        row = soup.tr(class_='firstRow')
        
        arr = soup('td', class_='destination')[0]
        arr = nonindent(arr.get_text())

        sch = soup('td', class_='status')[0]
        sch = nonindent(sch.get_text())

        status = soup('td', 'status')[1]
        status = status.get_text()
        if 'late' in status:
            status = 'Due ' + status[:5]
        elif 'early' in status:
            status = 'Due ' + status[:5]
        else:
            status = 'On time'

        platform = soup.tbody('td')[3]
        platform = platform.get_text()

        system('clear')
        print('-' * 20)
        print('Next arrival at ' + station)
        print('-' * 20)
        print('Origin:    ' + arr)
        print('Scheduled: ' + sch)
        print('Status:    ' + status)
        print('Platform:  ' + platform)
        print('-' * 20)
        
        sleep(1)

departures('SWI')

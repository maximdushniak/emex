import re
import csv
import sys
import time


import json

import requests
import lxml.html


def get_cookies(_url, _header):
    cookie = {}
    try:
        r1 = requests.post(url = _url, headers = _header)
        cookie = r1.cookies
    except:
        pass

    return cookie


def normalize_string(str='', pattern='[a-zA-Z0-9 /-]'):
    str = str.strip()
    p = re.compile(pattern)
    l = p.findall(str)
    return ''.join(l)


def get_listfromfile(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, dialect='excel', delimiter='\t')

        rows = [[normalize_string(column).upper() for column in row] for row in reader]

        return rows


def get_BestOriginalPrice(_art, _mark=''):
    param = {
    'detailNum': _art,
    'locationId':'18903' # минск
    }

    try:
        r = requests.post(url = link+'Find2/Find/FindByDetailNum',
                          headers = header,
                          cookies = cookie,
                          params = param
                          )

        data = r.json()['data']
        search_result = data['searchResult']
        detail = search_result['OriginalDetailsGroups']
        # result.update({'art':good['DetailNum'], 'mark':good['MakeName'], 'price':good['BestOriginalPrice']} for good in detail if (_mark=='' or _mark.upper() in good['MakeName'].upper())})
    except:
        return [{'searchart': _art,'searchmark': _mark, 'art':'', 'mark': '', 'price':0, 'error': sys.exc_info()[0]}]

    if len(detail) > 0:
        return [{'searchart': _art,'searchmark': _mark,'art':good['DetailNum'], 'mark':good['MakeName'], 'price':good['BestOriginalPrice'], 'error': ''} for good in detail if (_mark=='' or _mark.upper() in good['MakeName'].upper())]
    else:
        return [{'searchart': _art,'searchmark': _mark,'art':'', 'mark':'', 'price':0, 'error': ''}]


link = 'https://www.emex.ru/'

proxies = {'http': '188.165.141.151:80'}

header = {
    'Host': 'www.emex.ru',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    }

cookie = get_cookies(link, header)

if __name__ == '__main__':

    res = []
    res += (get_BestOriginalPrice('sadfasd', ''))
    res += (get_BestOriginalPrice('', ''))
    res += (get_BestOriginalPrice('oc47', ''))
    res += (get_BestOriginalPrice('oc95', 'knecht'))

    for i in res:
        print(i)

    # print(r.json())




    # doc = lxml.html.document_fromstring(r.text)
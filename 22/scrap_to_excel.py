import requests
from bs4 import BeautifulSoup
import pprint
import itertools
import re

BASE_URL = 'http://example.webscraping.com'


def make_links(soup):
    link_tags = soup.find_all('a', href=re.compile(r'/view/'))

    links = []
    for link_tag in link_tags:
        links.append(link_tag.get('href'))

    return links


def get_national_info(link):
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'lxml')

    national_info = []

    national_info.append(soup.select('#places_national_flag__row > td.w2p_fw > img')[0].get('src'))
    national_info.append(soup.select('#places_area__row > td.w2p_fw')[0].get('src'))
    national_info.append(soup.select('#places_population__row > td.w2p_fw')[0].get('src'))
    national_info.append(soup.select('#places_iso__row > td.w2p_fw')[0].get('src'))
    national_info.append(soup.select('#places_country__row > td.w2p_fw')[0].get('src'))
    national_info.append(soup.select('#places_capital__row > td.w2p_fw')[0].get('src'))
    national_info.append(soup.select('#places_continent__row > td.w2p_fw > a')[0].get('src'))
    national_info.append(soup.select('#places_tld__row > td.w2p_fw')[0].get('src'))
    national_info.append(soup.select('#places_currency_code__row > td.w2p_fw')[0].get('src'))
    national_info.append(soup.select('#places_currency_name__row > td.w2p_fw')[0].get('src'))
    national_info.append(soup.select('#places_phone__row > td.w2p_fw')[0].get('src'))
    national_info.append(soup.select('#places_postal_code_format__row > td.w2p_fw')[0].get('src'))
    national_info.append(soup.select('#places_postal_code_regex__row > td.w2p_fw')[0].get('src'))
    national_info.append(soup.select('#places_languages__row > td.w2p_fw')[0].get('src'))
    national_info.append(soup.select('#places_neighbours__row > td.w2p_fw > div')[0].get('src'))

    return national_info


def main():

    full_datas = []

    for i in itertools.count(0):    # itertools.count(0) 무한대로 i에 +1 해준다.
        res = requests.get(BASE_URL + '/index/' + str(i))
        soup = BeautifulSoup(res.text, 'lxml')
        links = make_links(soup)
        print('scrapping index: ', i)

        if not links:
            break


        national_infos = []

        for link in links:
            national_info = get_national_info(BASE_URL + link)
            national_infos.append(national_info)

        full_datas.append(national_infos)

    pprint.pprint(full_datas)


if __name__ == '__main__':
    main()

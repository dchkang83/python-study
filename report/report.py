import requests
from bs4 import BeautifulSoup
import csv
import pprint

BASE_URL = 'http://www.pythonscraping.com'


def create_list_from_table(table_tag):

    # CSV 파일로 만들기 위해서 2중 리스트 생성
    gifts = []

    # 헤더에 해당하는 1번째 로우 작성
    headers = []
    header_tag = table_tag.find('tr')
    for th_tag in header_tag.find_all('th'):
        if th_tag.text.strip() != 'Image':
            headers.append(th_tag.text.strip())     # strip 함수로 양쪽 공백 제거

    gifts.append(headers)

    # 선물 레코드 작성
    for tr_tag in table_tag.find_all('tr'):
        gift = []
        td_index = 0

        for td_tag in tr_tag.find_all('td'):
            td_index = td_index + 1

            if td_tag.text.strip() != '':
                # 좌우 공백을 제거하고 텍스트 속에 \n문자를 공백으로 변경
                td_text = td_tag.text.strip().replace('\n', ' ')
                
                # description의 값은 최초 5글자만 포함
                if td_index == 2:
                    td_text = td_text[:5]

                gift.append(td_text)
            elif td_tag.find('img') != '':
                continue

        if not gift:
            continue

        gifts.append(gift)

    # pprint.pprint(gifts)
    return gifts


def create_csv_file(lol, filename):
    # 이중 리스트의 내용을 CSV 파일로 저장
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for l in lol:
            writer.writerow(l)


def main():
    res = requests.get(BASE_URL + '/pages/page3.html')
    soup = BeautifulSoup(res.text, 'lxml')

    # 테이블 태그 확보
    table_tag = soup.find(id='giftList')

    gifts = create_list_from_table(table_tag)
    create_csv_file(gifts, 'gifts.csv')

    print('job completed..')


if __name__ == '__main__':
    main()

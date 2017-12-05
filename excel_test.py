import openpyxl


def find_parks_not_in_us():
    # 엑셀파일(워크북) 열기
    wb = openpyxl.load_workbook('D:\\python\\테스트.xlsx')

    # 워크시트 열기
    sheet = wb.get_sheet_by_name('Sheet1')

    # 결과를 저장할 리스트
    parklist = []

    # 파일을 로우 단위로 읽어 국가가 US가 아닌 로우를 파일로 쓴다.
    # 1. 파일을 읽을 범위를 결정
    # 2. 로우를 순회하면서 1003가 아닌 로우를 리스트로 만든다.
    for row in sheet[2:sheet.max_row]:
        print(row)
        if row[3].value != '1003':
            parklist.append(row)

    wb.close()  # don't forget!

    return parklist


def make_file(parklist):
    with open('D:\\python\\test.txt', 'w', encoding='UTF-8') as file:
        for item in parklist:
            park_str = make_parkstr(item)
            file.write(park_str + '\n')


def make_parkstr(t):
    result_str = ''

    for item in t:
        result_str += str(item.value) + '\t'

    return result_str


def main():
    print('GO')
    parklist = find_parks_not_in_us()
    make_file(parklist)
    print('parklist.txt 파일이 생성되었습니다.')


if __name__ == '__main__':
    main()

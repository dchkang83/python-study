import csv
import os


def save_and_remove_header(filename):
    # CSV 파일을 읽어 헤더를 제거하고 저장

    # CSV 파일을 리스트로 만든다.
    csv_rows = []
    with open(os.path.join('D:\\python\\csv-backup', 'core', filename), 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if reader.line_num == 1:
                continue    # 첫 번째 라인 스킵
            csv_rows.append(row)

    # 리스트를 파일로 쓴다.
    with open(os.path.join('D:\\python\\csv-backup', 'header-removed', filename), 'w', newline='') as file:
        writer = csv.writer(file)

        for row in csv_rows:
            writer.writerow(row)


def main():
    # 헤더가 제거된 파일이 저장될 폴더를 만든다.
    os.makedirs(os.path.join('D:\\python\\csv-backup', 'header-removed'), exist_ok=True)   # exist_ok 옵션은 폴더가 있어도 무시

    # 작업디렉토리의 모든 CSV 파일을 순회한다.
    for filename in os.listdir(os.path.join('D:\\python\\csv-backup', 'core')):
        if not filename.endswith('.csv'):
            continue    # 확장자가 csv가 아니면 스킵한다.

        print('saveing file : ' , filename)
        # 헤더가 제거된 파일을 저장한다.
        save_and_remove_header(filename)

    print('job completed..')


if __name__ == '__main__':
    main()

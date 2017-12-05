
def extract_text_from_subtitle(file_name):
    sub_title_contents = []

    file = open(file_name, 'r')
    for line in file:   # file 자체를 roof 돌리면 line을 리턴시켜준다.
        line = line.replace('\n', '')
        if len(line) < 3 and line.isnumeric():
            continue    # pass 로 구현해도 됨.
        elif line.count(':') > 2 and line.count('-->') > 0:
            pass
        elif line == '':
            pass
        else:
            sub_title_contents.append(line)     # 한문장이 완료되었을때로 변경해보자.

    file.close()
    return sub_title_contents


def make_file_and_save(content, file_name, ext='txt'):
    # 리스트로 파일을 생성
    with open(file_name + '.' + ext, 'w') as file:
        for line in content:
            file.write('%s\n' % line)   # python2의 포멧 (3으로 변경하자)


def main():
    file_name = 'subtitle.srt'
    subtitle_contents = extract_text_from_subtitle(file_name)
    make_file_and_save(subtitle_contents, file_name, 'txt')
    print('job completed..')


if __name__ == '__main__':
    main()
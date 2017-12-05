import codecs
import re

# Create email regex.
email_regex = re.compile(r'''(
[a-zA-Z0-9._%+-]+			# username
@							# @ symbol
[a-zA-Z0-9.-]+				# domain name
(\.[a-zA-Z]{2,4}){1,2}		# dot-something
)''', re.VERBOSE)

def extract_text_from_subtitle(file_name):
    sub_title_contents = []

    # file = codecs.open("D:\\temp\\megabox\\test.txt", "r", "utf-8")
    file = codecs.open("D:\\temp\\megabox\\in\\201\\" + file_name, "r", "CP949")

    contents = email_regex.findall(file.read())

    # print(contents)

    # for line in file:   # file 자체를 roof 돌리면 line을 리턴시켜준다.
    #     line = line.replace('\n', '')
    #     #print(line)
    #     sub_title_contents.append(line)  # 한문장이 완료되었을때로 변경해보자.

    file.close()
    return sub_title_contents


def make_file_and_save(content, file_name, ext='txt'):
    # 리스트로 파일을 생성
    with open(file_name + '.' + ext, 'w') as file:
        for line in content:
            file.write('%s\n' % line)   # python2의 포멧 (3으로 변경하자)


def main():
    file_name = 'mega201.platform - 1.txt'
    subtitle_contents = extract_text_from_subtitle(file_name)
    #make_file_and_save(subtitle_contents, file_name, 'txt')
    print('job completed..')


if __name__ == '__main__':
    main()

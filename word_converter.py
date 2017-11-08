
"""
- 간단한 단어 번역기 만들기 - 단어 첫 글자를 마지막으로 옮기고 'ay'를 추가
단어 하나를 입력 받는다. (input() 함수 사용)
공백을 입력하거나 글자가 아닌 것을 입력했을 때 "invalid word!"라고 출력
입력된 단어를 수정하여 완성된 글자를 출력
"""

original = input("Enter a word:")

# isalpha() 문자나 글자인지 체크
if len(original) > 0 and original.isalpha():
    # do your job
    # original = original[1:] + original[0] + 'ay'
    first_char = original[0]
    new_word = original[1:] + first_char + 'ay'
    print(new_word)

else:
    print('invalid word!')

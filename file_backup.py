import os
import zipfile

def backup_to_zip(folder):
    # 폴더내의 파일을 zip 파일로 백업

    # 작업디렉토리 이동
    os.chdir(folder)
    print('Current working directory is ' + os.getcwd())

    # zip 파일명 생성
    zip_filename = os.path.basename(folder) + '.zip'
    print('Creating %s' % zip_filename)

    # backup 폴더 생성
    os.mkdir('..\\backup')

    # backup 폴더에 백업파일을 생성
    backupzip = zipfile.ZipFile('..\\backup\\' + zip_filename, 'w')

    # 작업디렉토리를 순회하면서 백업파일을 생성
    # 1. 확장자가 .jpg 파일은 백업하지 않는다.
    for foldername, subfolders, filenames in os.walk('.'):

        # 현재폴더를 ZIP파일에 추가
        backupzip.write(foldername)

        # 하위폴더를 ZIP파일에 추가
        for subfolder in subfolders:
            #backupzip.write(foldername + '\\' + subfolder)
            backupzip.write(os.path.join(foldername, subfolder))    # os.path.join : OS에 맞게 PATH 적용해줌

        # 하위 폴더의 파일들을 ZIP파일에 추가
        for filename in filenames:
            if filename.endswith('.jpg'):
                print('skip compressing file : ' + filename)
                continue
            backupzip.write(os.path.join(foldername, filename))

    backupzip.close()


def main():
    backup_to_zip('D:\\temp\\python_test\\test_in')


if __name__ == '__main__':
    main()

#os.listdir(path) 파일목록 리스트로 전달
#os.chdir(path) 작업 디렉토리 변경



from os import rename, listdir, chdir
import time

class FileRenaming:

    __FILES = listdir('..\\..\\image\\test\\')

    def __init__(self):
        chdir('..\\..\\image\\test\\')  # 작업 디렉토리가 현재 작업중인 파이썬 파일이 있는 위치로 되어 있으므로 변경 필요
        self.file_num = 1
        self.count = 0
        self.tmp=[]
        self.file_renaming()

    def file_renaming(self):
        for file in FileRenaming.__FILES:
            self.tmp.append(int(file.split('.')[0]))

        self.tmp.sort()

        for i in self.tmp:
            self.tmp[self.count] = str(i)+'.jpg'
            self.count += 1

        files=self.tmp

        for file_name in files:
            new_name = str(self.file_num) + '.jpg'
            rename(file_name, new_name)
            self.file_num += 1

        print('파일 이름이 모두 변경되었습니다.')

stater = FileRenaming()
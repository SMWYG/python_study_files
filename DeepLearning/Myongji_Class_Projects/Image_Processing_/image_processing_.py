# resize() => 비율도 영향줌
# thumbnail() => 비율은 그대로 가로 비율을 기준으로 살려줌
# 나머지
# 회색 rgb(128,128,128)
# 1. 이미지 파일명 다 가져오기 (listdir())
# 2. 이미지 open 후 객체 가져오기 (Image.open + for문 사용해서 모두 가져와서 리스트에 담기)
# 3.

from PIL import Image
from os import listdir


class ImagePreprocess:

    __DATA_PATH = "C:\\Users\\dahan\\Downloads\\"

    def __init__(self):
        self.imgsize = (32, 32)
        self.image_files = listdir(ImagePreprocess.__DATA_PATH)
        self.image_preprocess()

    def image_preprocess(self):
        self.data_change()
        self.resize()
        self.rgb2gray() #여기서 값 추가 0.5로

    def resize(self):
        i = Image.open('C:\\Users\\dahan\\Downloads\\6.jpg')
        i.thumbnail(self.imgsize)
    def rgb2gray(self):


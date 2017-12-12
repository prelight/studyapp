import sys
import numpy as np
import os.path
import shutil
import os, glob, random
from PIL import Image

EXE_PATH = os.path.dirname(os.path.abspath(__file__))
photo_size = 75 # 画像サイズ

def main():
    for angle in range(-20, 21, 5):
        print(angle)
    sys.exit()

    #画像の回転
    f= os.path.join(EXE_PATH, "sakura-ok\\13465595245.jpg")
    img = Image.open(f)
    img = img.convert("RGB") # 色空間をRGBに
    img = img.resize((photo_size, photo_size))
    img_angle = img.rotate(10)
    img_angle.save("toriaezu_sakura1.jpg");

    #if not rotate: continue
    ## 角度を少しずつ変えた画像を追加 --- (1)
    #for angle in range(-20, 21, 5):
    #  # 角度を変更
    #  if angle != 0:
    #    img_angle = img.rotate(angle)

def main2():
    # 画像ファイルを読む --- (4)
    f= os.path.join(EXE_PATH, "sakura-ok\\13465595245.jpg")
    img = Image.open(f)
    img = img.convert("RGB") # 色空間をRGBに合わせる
    # 同一サイズにリサイズ
    img = img.resize((photo_size, photo_size)) #サイズが違うファイルがあった時の為かな・・
     
    data = np.asarray(img)
    data = data / 256 # 正規化する --- (6)
    data = data.reshape(photo_size, photo_size, 3)#これは必要？←必要かな・・←必要性がいまいち・・
    #print(img)
    print(os.getcwd())  #カレントディレクトリ
    ##img = np.array([3,4,5,5])
    #img = [3,4,5,5]
    #data = np.asarray(img)
    #img[2] = 6
    #print(img)
    #print(data)


def main1():
    print(os.getcwd())  #カレントディレクトリ
    path = os.path.join("201712_week2", "sakura-ok", "*.jpg")

    files = glob.glob(path)
    #print("hello!")
    print([ os.path.basename(f) for f in files ])



if __name__ == '__main__':
    main()


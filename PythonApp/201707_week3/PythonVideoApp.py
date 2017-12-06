
# -*- coding: utf-8 -*-
import os
import re
import sys
import requests
import shutil
import os.path
import collections
import asyncio
from bs4 import BeautifulSoup

VIDEO_PATH = "C:\\Users\\tokamoto\\Desktop\\videofile" #"J:\\video" #"C:\\Users\\okamoto\\Desktop\\VIDEOPATH"
#VIDEO_PATH = "C:\\Users\\okamoto\\dwhelper\src"
DEST_PATH = "C:\\Users\\tokamoto\\Desktop\\videofiledst" #"J:\\video\\video005"#"C:\\Users\\okamoto\\Desktop\\DEST"
DEST_IMG = "J:\\video\\video_image\\image005"

def get_video_list(path):
    video_list = []
    image_list = []
    ext_list = ['.wmv', '.mp4', '.avi', '.flv', '.rmvb', '.m4v', '.mkv', '.webm']
    for (root, dirs, files) in os.walk(path): # 再帰的に探索
        for file in files: # ファイル名だけ取得
            root, ext = os.path.splitext(file)
            if ext.lower() in ext_list:
                video_list.append(file)
            if ext.lower() == ".jpg":
                image_list.append(file)
    return video_list, image_list


def get_code_name(file_name):
    delimiter = '[]._'
    trans_name = file_name.translate(str.maketrans(delimiter, ' ' * len(delimiter)))
    words = [item for item in trans_name.split(' ') if item is not '']
    
    #第1条件 デリミタで区切りられた文字列の中にAAA-999があること
    pattern = r"^[a-zA-Z]+-\d+$"
    for word in words:
        matchObj = re.match(pattern , word)
        if matchObj != None:
            return word 

    #第2条件 デリミタで区切りられた文字列の先頭がAAA999であること
    pattern = r"^([a-zA-Z]+)(\d+)$"
    matchObj = re.match(pattern , words[0])
    if matchObj != None:
        return "{0}-{1}".format(matchObj.group(1), matchObj.group(2))

    return None


def is_check_title(title):
    if len(title) > 2:
        sub = title[0:2]
        if (sub == "【数" or sub == "【D"):
            return False
    return True


async def get_title_and_image_from_web(code, getparams):
    getparams["searchstr"] = code
    title = None
    image = None

    #検索ページからtitle取得
    url = "http://www.dmm.co.jp/search/"    
    html = requests.get(url, params=getparams)
    soup = BeautifulSoup(html.text, 'html.parser')
    spans = soup.select("span[class='img']")
    for span in spans:
        img = span.select_one("img")
        search = str.lower(code.replace("-", ""))
        if search in img.attrs["src"]:
            title = img.attrs["alt"]
            if (is_check_title(title)):
                url = span.parent.attrs["href"]
                break

    #詳細ページからimage取得
    if title != None:
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        image = soup.select_one("#sample-video").select_one("a").attrs["href"]

    print("code={0}, title={1}".format(code, title))
    return code, title, image


def get_getrequest_params():
    url = "http://www.dmm.co.jp/mono/"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    hidden_items = soup.select("input[type='hidden']")
    params = {"analyze" : "", "redirect" : "", "enc" : ""}
    for elm in hidden_items:
        if elm.attrs["name"] in params.keys():
            params[elm.attrs["name"]] = elm.attrs["value"]
    #add_params = {"sort" : "ranking", "limit" : "30", "view" : "package", "category" : "mono"}
    add_params = {"sort" : "", "limit" : "", "view" : "", "category" : "mono"}
    params.update(add_params)
    return params


def move_and_rename_file(code, file, title):
    #タイトル
    title = title[0:70] + "..." if len(title) > 70 else title
    if os.path.isfile(file) or os.path.isdir(file):
        ext = os.path.splitext(file)[1] if os.path.isfile(file) else ""
        new_name = "[{0}] {1}{2}".format(code.upper(), title, ext)
        shutil.move(file, os.path.join(DEST_PATH, new_name))        


def download_image(image_url, image_name):
    res = requests.get(image_url) 
    if res.status_code == 200: 
        #ext = os.path.splitext(image_url)[1]
        with open(image_name, 'wb') as file: 
            file.write(res.content) 


async def get_title_and_image(codes):
    #return [("JUY-019","aass",""), ("ASD-223","bbb","")  ]
    params = get_getrequest_params()
    cors = [get_title_and_image_from_web(code, params) for code in codes]
    results = await asyncio.gather(*cors)
    return results


def main():
    print("start")
    #対象ファイルとコード取得
    file_names = os.listdir(VIDEO_PATH)
    exist_codes = [c for c in [get_code_name(f) for f in os.listdir(DEST_PATH)] if c]
    #exist_codes = [get_code_name(f) for f in os.listdir(DEST_PATH)]
    code_names = {get_code_name(f):[os.path.join(VIDEO_PATH, f)] for f in  file_names}
    code_names = {c:a for c,a in code_names.items() if c and (not c in exist_codes)}

    #webから非同期でタイトル、imageパス取得
    loop = asyncio.get_event_loop()
    code_infos = loop.run_until_complete(get_title_and_image(code_names.keys()))
    for code_info in code_infos:
        code, title, image_url = code_info
        code_names[code].append(title)
        code_names[code].append(image_url)
   
    #image保存&ファイル名変更移動
    for code, val in code_names.items():
        file, title, image_url = val
        try:
            ext = os.path.splitext(image_url)[1]#拡張子
            image_name = os.path.join(DEST_IMG, code.upper() + ext)
            download_image(image_url, image_name)
            move_and_rename_file(code, file, title)
            print("move: " + code)
        except:
            print("{0}でエラーが発生:{1}".format(code, sys.exc_info()))

if __name__ == '__main__':
    main()

# Flickrで写真を検索して、ダウンロードする
from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# API Keyの設定（書き換えてご利用ください）
key = "0ab71de3f7019af0e35dd66135e87a63"
secret = "dacb4ffdb05d7b75"
# ダウンロード後の待機時間（1以上を指定）
wait_time = 1 

# キーワードをチェックする
#if len(sys.argv) < 2:
#  print("python dl.py (keyword)")
#  sys.exit()
keyword = "tiger"#sys.argv[1]
savedir = "201712_week2/" + keyword
if not os.path.exists(savedir):
  os.mkdir(savedir) # フォルダーを作る

# Flickr APIで写真を検索
flickr = FlickrAPI(key, secret, format='parsed-json')
res = flickr.photos.search(
  text = keyword,           # 検索語
  per_page = 10,           # 取得件数（最大500件）
  media = 'photos',         # 写真を検索
  sort = "relevance",       # 検索語の関連順に並べる
  safe_search = 1,          # セーフサーチ（1を指定）
  extras = 'url_q,license') # 取得する

# 検索結果を確認
photos = res['photos']
pprint(photos)
try:
  # 1つずつ画像をダウンロードする
  for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir+'/'+photo['id']+'.jpg'
    if os.path.exists(filepath): continue
    print(str(i + 1) + ":download=", url_q)
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
except:
  import traceback
  traceback.print_exc()


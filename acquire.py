import feedparser
from pathlib import Path
import shutil
import pprint
import time


def acquire(args):
    # テンプレに引数を割り当ててXMLのURLを生成し、XMLを解析する。
    url = 'https://www.youtube.com/feeds/videos.xml?channel_id=' + str(args)
    xml = feedparser.parse(url)
    urlid = [entry['yt_videoid'] for entry in xml['entries']]

    # pprint.pprint(xml, depth=1)
    # print(urlid)

    # 抽出したIDの配列から最新のものを取り出す
    firstid, *otherid = urlid
    # print(firstid)

    # 最新のIDを元に動画のURLを生成する。
    youtube_url = 'https://www.youtube.com/watch?v=' + str(firstid)
    # print(youtube_url)

    # 最新のIDををとりあえずファイルに出力しておく
    myfile = Path('LatestVideoId.txt')
    myfile.touch(exist_ok=True)
    setid = open('LatestVideoId.txt', 'w', encoding='utf-8')
    setid.write(firstid)
    setid.close()

    return youtube_url

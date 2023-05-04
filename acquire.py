import feedparser
from pathlib import Path
import shutil
import pprint
import urllib.parse
import UrlQueryAdd


def acquire(args):
    # テンプレに引数を割り当ててXMLのURLを生成する。ちゃんとurllib使ってえらい
    # parsedurl = urllib.parse.urlparse('https://www.youtube.com/feeds/videos.xml')
    # queryurl = urllib.parse.parse_qs(parsedurl.query, True)
    # queryurl['channel_id'] = str(args)
    # encoded = urllib.parse.urlencode(queryurl, True)
    # url = urllib.parse.ParseResult(parsedurl.scheme, parsedurl.netloc, parsedurl.path, parsedurl.params, encoded,
    #                                parsedurl.fragment).geturl()
    url = UrlQueryAdd.urlqueryadd('https://www.youtube.com/feeds/videos.xml', 'channel_id', args)

    # print(url)

    # 先で生成したURLを使ってRSSをparseする。
    xml = feedparser.parse(url)
    urlid = ([entry['yt_videoid'] for entry in xml['entries']])[0]

    # pprint.pprint(xml, depth=1)
    # print(urlid)

    # 最新のIDを元に動画のURLを生成する。
    youtube_url = 'https://www.youtube.com/watch?v=' + str(urlid)
    # print(youtube_url)

    # 最新のIDををとりあえずファイルに出力しておく
    # ファイルがないときは新規で作成
    myfile = Path('LatestVideoId.txt')
    myfile.touch(exist_ok=True)
    setid = open('LatestVideoId.txt', 'w', encoding='utf-8')
    setid.write(urlid)
    setid.close()

    return youtube_url

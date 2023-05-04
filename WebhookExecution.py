import requests
import json
import os.path
import feedparser
import UrlQueryAdd
import pprint


def webhookrun(channel_id):
    # WebHookURLの取得 定義がない場合は即終了
    try:
        with open(r"webhook.ini") as f:
            readfile = open('webhook.ini', 'r', encoding='utf-8')
            webhookurl = readfile.read()
            print(webhookurl)
    except FileNotFoundError:
        print("WebHookURLが定義されているファイルがありません。")
        return

    # Embed用の材料を取得 二度手間かも
    xml_url = UrlQueryAdd.urlqueryadd('https://www.youtube.com/feeds/videos.xml', 'channel_id', channel_id)
    xml = feedparser.parse(xml_url)

    # Embedで使うものを変数に突っ込む
    embed_title = ([entry['title'] for entry in xml['entries']])[0]
    embed_description = ([entry['summary'] for entry in xml['entries']])[0]
    embed_url = ([entry['link'] for entry in xml['entries']])[0]
    embed_timestamp = ([entry['updated'] for entry in xml['entries']])[0]
    embed_footer_text = ([entry['authors'] for entry in xml['entries']])[0][0]['name']
    embed_thumbnail_url = ([entry['media_thumbnail'] for entry in xml['entries']])[0][0]['url']
    embed_author_name = ([entry['authors'] for entry in xml['entries']])[0][0]['name']

    # Webhookの内容を作成する
    content = {
        "username": embed_author_name,
        "embeds": [
            {
                "title": embed_title,
                "description": embed_description,
                "url": embed_url,
                "timestamp": embed_timestamp,
                "color": 5620992,
                "footer": {
                    "text": embed_footer_text
                },
                "image": {
                    "url": embed_thumbnail_url
                },
                "thumbnail": {
                    "url": embed_thumbnail_url
                },
                "author": {
                    "name": embed_author_name,
                    "url": embed_url
                },
            }
        ]
    }

    # print(content)

    # 作成したものをDiscordに投げる
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(webhookurl, data=json.dumps(content), headers=headers)
        response.raise_for_status()
        print(response.status_code)
    except requests.exceptions.RequestException as e:
        print("何かがおかしいよ", e)

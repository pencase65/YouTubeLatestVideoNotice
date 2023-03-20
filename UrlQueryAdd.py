import urllib.parse


def urlqueryadd(baseurl, name, id):
    # baseurl : パラメータを付けたいベースのURL
    # name : パラメータの変数名 例えば「?p=2」のpとか
    # id : パラメータの値 例えば「?p=2」の2とか
    parsedurl = urllib.parse.urlparse(baseurl)
    query = urllib.parse.parse_qs(parsedurl.query, True)
    query[str(name)] = str(id)
    encoded = urllib.parse.urlencode(query, True)
    url = urllib.parse.ParseResult(parsedurl.scheme, parsedurl.netloc, parsedurl.path, parsedurl.params, encoded,
                                   parsedurl.fragment).geturl()

    return url

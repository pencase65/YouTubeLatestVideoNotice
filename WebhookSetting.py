from pathlib import Path


def webhooksetting(webhookurl):
    dirname = Path(__file__).resolve().parent
    myfile = Path(dirname.joinpath('webhook.ini'))
    myfile.touch(exist_ok=True)
    seturl = open(dirname.joinpath('webhook.ini'), 'w', encoding='utf-8')
    seturl.write(webhookurl)
    seturl.close()

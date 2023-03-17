import requests


def is_sensitive(word: str) -> bool:
    with requests.post("https://music.163.com/api/cloudsearch/pc", headers='',
                       data={"s": word, "type": 1, "limit": 30, "offset": 0, "total": True}, files=None) as req:
        req.encoding = "utf-8"
        try:
            data = req.json()['result']
        except KeyError:
            return True
    return True if data == {} else False


def is_not_sensitive(word: str) -> bool:
    return not is_sensitive(word)

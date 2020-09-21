import requests


class HttpClient(object):
    @staticmethod
    def post(url, content, headers=None):
        if headers is None:
            headers = {}
        client = requests.post(url, content, headers=headers)
        return client.text

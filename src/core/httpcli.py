import httpx


class HttpCli(object):
    def __init__(self):
        self.client = httpx.Client()

    def get(self, url):
        response = self.client.get(url)
        return self._dump_response(response)

    def post(self, url, data):
        response = self.client.post(url, json=data)
        return self._dump_response(response)

    @staticmethod
    def _dump_response(response):
        print(response)
        return {
            "status": response.status_code,
            "content": response.content,
        }

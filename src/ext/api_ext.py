from IPython.core.magic import Magics, magics_class, line_magic
from IPython.display import JSON
from core.httpcli import HttpCli

client = HttpCli()


@magics_class
class APIMagics(Magics):

    @line_magic
    def get(self, line):
        url = line
        response = client.get(url)
        return JSON(response)

    @line_magic
    def post(self, line):
        url, data = line.split(' ', 1)
        response = client.post(url, data)
        return JSON(response)


def load_ipython_extension():
    ipython = get_ipython()
    ipython.register_magics(APIMagics)
    print('%get  /path/to/endpoint?param=value')
    print('%post /path/to/endpoint data={} header={}')

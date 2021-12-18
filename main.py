from typing import Counter
from rpa import web

if __name__ == "__main__":
    web.open_url('like_url', True)
    while (True):
        web.view(8)
        web.next()

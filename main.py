from typing import Counter
from rpa import web

if __name__ == "__main__":
    web.open_url('like_url', True)
    counter = 0
    reposition = 60
    while True:
        web.likeable()
        print("Likeable")
        web.open_url('passport_url', False)
        web.timer()
        web.passport()

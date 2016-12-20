from contextlib import contextmanager

class Query(object):
    def __init__(self,name):
        self.name = name

    def query(self):
        print("query info about %s ... " %self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


with create_query('jiang') as q:
    q.query()


from contextlib import closing
from urllib.request import urlopen

with closing(urlopen("http://www.ifeng.com/")) as page:
    for line in page:
        print(line)
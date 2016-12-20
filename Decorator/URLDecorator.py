import functools,asyncio

def get(path):
    '''
    Define decorator @get('/path')
    :param path:
    :return:
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            return func(*args,**kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__  = path
        return wrapper
    return decorator

class RequestHandler(object):
    def __init__(self,app,fn):
        self._app = app
        self._func = fn

    @asyncio.coroutine
    def __call__(self, request):
        r = yield from self._func(**kw)
        return r
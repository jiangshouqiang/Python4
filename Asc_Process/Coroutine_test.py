import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world !(%s)' % threading.current_thread())
    s = input('Please input value :')
    # yield from asyncio.sleep(1)
    print("hello again ! (%s , %s )" % (threading.current_thread(),s))

loop = asyncio.get_event_loop()
tasks = [hello(),hello()]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()
import asyncio

# @asyncio.coroutine
# def hello():
#     print('hello world!')
#     r = yield from asyncio.sleep(1)
#     print("Hello , again!")

async def hello():
    print('hello world!')
    r = await asyncio.sleep(1)
    print("Hello , again!")

# get EventLoop
loop = asyncio.get_event_loop()
# run coroutine
loop.run_until_complete(hello())
loop.close()
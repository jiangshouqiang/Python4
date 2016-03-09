import random,time,queue
from multiprocessing.managers import BaseManager
#send task list
task_queue = queue.Queue()
#get resut list
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable(lambda:result_queue))

#bind prot 5000,set check number
manager = QueueManager(address=('',5000),authkey=b'abc')
#start queue
manager.start()
#access Queue by intenent
task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    r = result.get(timeout=10)
    print("Result:%s" % r)

manager.shutdown()
print("exit")
import time,threading,multiprocessing
local_thread = threading.local()

# lock = threading.Lock()

def change_it(n):
    # global balance
    balance = local_thread.balance
    balance += n
    balance -= n
def run_thread(n):
    local_thread.balance = 0
    for i in range(10000000):
        change_it(n)
    print(local_thread.balance)
        # lock.acquire()
        # try:
        #     change_it(n)
        # finally:
            # lock.release()

print(multiprocessing.cpu_count())
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
# print(local_thread.balance)

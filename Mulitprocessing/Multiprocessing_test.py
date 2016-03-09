import os
#import multiprocessing
from multiprocessing import Process

# print("process (%s) start ..." % os.getpid())
#
# pid = os.fork()
#
# if pid == 0 :
#     print("I am child process (%s) and my parent is %s ." % (os.getpid(),os.getppid()))
# else:
#     print("I (%s) just created a child")
def run_proc(name):
    print('Run child process %s (%s) ...' %(name,os.getpid()))

if __name__ == '__main__':
    os.fork()
    print("Parent process %s." %os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print("Child process end.")

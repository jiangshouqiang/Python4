from multiprocessing import Process
import os

def run_proc(name):
    print("Run child process %s (%s) " %(name,os.getppid()))

if __name__ == "__main__":
    print("parent process is %s " % os.getpid())
    p = Process(target=run_proc,args=('jiang',))
    print("start")
    p.start()
    p.join()
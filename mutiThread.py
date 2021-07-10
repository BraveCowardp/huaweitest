import threading

lockA = threading.Lock()
lockB = threading.Lock()
lockC = threading.Lock()
lockD = threading.Lock()
runFlag = threading.Event()

lockB.acquire()
lockC.acquire()
lockD.acquire()

def printA(n):
    i=0
    while(True):
        lockA.acquire()
        i+=1
        if i > n:
            break
        print('A',end='')
        lockB.release()
    runFlag.clear()
    lockB.release()

def printB():
    while(True):
        lockB.acquire()
        if runFlag.isSet()==False:
            break
        print('B',end='')
        lockC.release()
    lockC.release()

def printC():
    while(True):
        lockC.acquire()
        if runFlag.isSet()==False:
            break
        print('C',end='')
        lockD.release()
    lockD.release()

def printD():
    while(True):
        lockD.acquire()
        if runFlag.isSet()==False:
            break
        print('D',end='')
        lockA.release()
    lockA.release()

while(True):
    try:
        n = int(input())
    except:
        break

    job1=threading.Thread(target=printA,args=(n,))
    job2=threading.Thread(target=printB)
    job3=threading.Thread(target=printC)
    job4=threading.Thread(target=printD)

    runFlag.set()
    job1.start()
    job2.start()
    job3.start()
    job4.start()

    job1.join()
    job2.join()
    job3.join()
    job4.join()
    print('')
#coding=utf-8
'''
Created on 2015年3月30日

@author: hongtu_zang
'''
import time
from multiprocessing import Process,Queue

MSG_QUEUE = Queue(5)

def startA(msgQueue):
    while True:
        if msgQueue.empty() > 0:
            print 'queue is empty %d' % (msgQueue.qsize())
        else:
            msg = msgQueue.get()
            print 'get msg %s' % msg
        time.sleep(1)

def startB(msgQueue):
    while True:
        msgQueue.put('Hello World')
        print 'put Hello World queue size is %d' % (msgQueue.qsize(),)
        time.sleep(3)
        
if __name__ == '__main__':
    processA = Process(target=startA, args=(MSG_QUEUE,))
    processB = Process(target=startB, args=(MSG_QUEUE,))
    
    processA.start()
    print "Process A starting..."
    
    processB.start()
    print "Process B starting..."
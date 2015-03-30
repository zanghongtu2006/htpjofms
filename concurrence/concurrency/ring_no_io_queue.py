#coding=utf-8
'''
Created on 2015年3月30日

@author: hongtu_zang
'''
import threading, Queue

def pid():
    return threading.currentThread()

class Loop(threading.Thread):
    def __init__(self, s, cin, cout):
        threading.Thread.__init__(self)
        self.cin = cin
        self.cout = cout
        self.s = s
    def run(self):
        while True:
            r = self.cin.get()
            self.cout.put(r)
            if r > 0:
                print(": Proc: <%s>, Seq#: %s, Msg#: %s .." % (pid(), self.s, r))
            else:
                print("* Proc: <%s>, Seq#: %s, Msg#: terminate!" % (pid(), self.s))

class MLoop(threading.Thread):
    def __init__(self, s, cin):
        threading.Thread.__init__(self)
        self.cin = cin
        self.s = s
    def run(self):
        while True:
            r = self.cin.get()
            if r > 0:
                print("> Proc: <%s>, Seq#: %s, Msg#: %s .." % (pid(), self.s, r))
            else :
                print("@ Proc: <%s>, Seq#: %s, ring terminated." % (pid(), self.s))
    
def run_benchmark(n, m):
    firstP = cin = Queue.Queue()
    for s in xrange(1, n):
        seqn = s
        cout = Queue.Queue()
        print("*> s = %d" % (seqn, ))
        t = Loop(seqn, cin, cout)
        t.setDaemon(False)
        t.start()
        cin = cout
    else:
        seqn = n + 1
        print("$> s = %d" % (seqn, ))
        t = MLoop(seqn, cin)
        t.setDaemon(False)
        t.start()
    for r in xrange(m -1, -1, -1):
        firstP.put(r)


if __name__ == '__main__':
    run_benchmark(3, 5)
#coding=utf-8
'''
Created on 2015年3月30日

@author: hongtu_zang

start a new process
'''

import processing

def run_benchmark(n, m):
    firstP = cin = processing.Queue()
    # from 1 to n, start loop process
    for s in xrange(1, n):
        print "s = %d" % s
        seqn = s
        cout = processing.Queue()
        print ("*> s = %d" % (seqn, ))
        p = processing.Process(target = loop, args = [seqn, cin, cout])
        p.start()
        cin = cout
    else:
    # for n, start mloop process
        seqn = s + 1
        print("$> s = %d" % (seqn, ))
        p = processing.Process(target=mloop, args = [seqn, cin])
        p.start()
    for r in xrange(m-1, -1, -1):
        print ("+ sending Msg# %d" % r)
# do not know how to use
        firstP.put(r)
    p.join()

def loop(s, cin, cout):
    while True:
        r = cin.get()
        cout.put(r)
        if r > 0:
            print (": Proc: <%s>, Seq#: %s, Msg#: %s .." % (pid(), s, r))
        else :
            print ("* Proc: <%s>, Seq#: %s, Msg#: terminate!" % (pid(), s))

def pid():
    return processing.currentProcess()

def mloop(s, cin):
    while True:
        r = cin.get()
        if r > 0:
            print("> Proc: <%s>, Seq#: %s, Msg#: %s .." % (pid(), s, r))
        else:
            print("@ Proc: <%s>, Seq#: %s, ring terminated." % (pid(), s))
    
if __name__ == '__main__':
    run_benchmark(3, 5)
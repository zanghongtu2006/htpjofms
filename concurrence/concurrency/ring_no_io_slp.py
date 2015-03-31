#coding=utf-8
'''
Created on 2015年3月30日

@author: hongtu_zang
'''
import stackless as SL

def pid():
    return repr(SL.)

def loop(s, cin, cout):
    while True:
        r = cin.receive()
        cout.send(r)
        if r > 0:
            print(": Proc: <%s>, Seq#: %s, Msg#: %s .." % (pid(), s, r))
        else :
            print("* Proc: <%s>, Seq#: %s, Msg#: terminate!" % (pid(), s))

if __name__ == '__main__':
    pass
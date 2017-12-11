import threading, Queue
from random import *
import requests
import os

def ball_out(btcdat,epochs=200,buyp = -1):
    dat_arr = []
    havebtc = 0
    dat_len = 0
    pnl = 0
    numt = -1
    unsold = False
    while dat_len < epochs:
        if dat_len >= epochs-2 and havebtc == 1:
            unsold = True
            dat_len = 100
        if numt > 30:
            if havebtc == 0:
                print("havent bought btc, reseting buyp")
                numt = 0
                dat_arr = []
            if havebtc ==1:
                print("unable to sell btc, reseting flux")
                flux = flux/3
        if numt > 60:
            flux = 7
        #r= requests.get("http://localhost:5000/live-data")
        r = requests.get("http://finvibby.herokuapp.com/live-data")
        got_price = r.json()[1]
        if type(got_price) == int:
            dat_arr.append(got_price)
            if len(dat_arr) == 10:
                buyp = (min(dat_arr) + sorted(dat_arr)[1])/2
                flux = (max(dat_arr) - buyp)/2
                print("FLUX is ",flux)
            if len(dat_arr) > 10:
                if got_price <= buyp and havebtc == 0:
                    print("bought at ", got_price)
                    havebtc = 1
                    numt = 0
                if got_price > buyp + flux and havebtc == 1:
                    print("sold at ",got_price)
                    pnl+=(got_price-buyp)
                    havebtc = 0
                    numt = 0
                    dat_arr = []
        dat_len +=1
        numt +=1
        if unsold == True and havebtc == 0:
            print("sold last bit")
            dat_len = epochs+1000
        print("itercount " + str(dat_len) + " dead iters " + str(numt))

    print("-----------------------")
    os.system("say 'done'")
    print(pnl)
    return pnl

def func1(num, q,kg):
    for i in range(10):
        x = kg.get()
        if x == 1:
            print("should end now")
        num = randint(0,5)
        print(num)
        q.put(num)

def func2(num, q,kg):
    for i in range(10):
        num = q.get()
        if num == 1:
            print("hit")
            kg.put(1)
        else:
            kg.put(0)
def storeinarray(btcdat):
    array = []
    for i in range(500):
        array.append(btcdat.get(timeout=0.5))
    return len(array)
num = 2
q = Queue.Queue()
kg = Queue.Queue()
kg.put(0)
thread1 = threading.Thread(target=func1,args=(num,q,kg))
thread2 = threading.Thread(target=func2,args=(num,q,kg))
btcdat = Queue.Queue()
btcdat.put(-1)
thread3 = threading.Thread(target=ball_out,args=(btcdat))
thread4 = threading.Thread(target=storeinarray,args=(btcdat))
#thread1.start()
#thread2.start()
thread3.start()
thread4.start()

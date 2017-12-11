from multiprocessing import Process, Queue
from random import *
import sys
import time


def create():
    global rocket
    print ('start creating')
    while True:
        rocket = randint(0,100)
        time.sleep(0.2)

def read():
    print('start read')
    print(rocket)
    if rocket == 50:
        print("target hit")

def f1():
    global x
    x = []
    while len(x) < 10:
        x.append(randint(0,10))
def f2():
    print(x)


if __name__=='__main__':

    print("-----------------")
    p1 = Process(target=f1)
    p1.start()
    p2 = Process(target=f2)
    p2.start()

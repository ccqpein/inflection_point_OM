#!/usr/env python
# -*- coding=utf-8 -*-

import random
import sys

size = [10,10]
pobli = 0
repeat_time = 100
pobli_step=0.01

def repeat(fun):
    def inner(*argv):
        global repeat_time
        liss = []
        while repeat_time>0:
            liss.append(fun(*argv))
            repeat_time -= 1
        return liss
    return inner

def process(pobli):
    for i in range(size[0]):
        for ii in range(size[1]):
            if random.random() <= pobli:
                if ii == size[1]-1:
                    #print("done and ",pobli)
                    return pobli
                else:
                    continue
            else:
                break
    
@repeat
def pobliplus(pobli):
    lis = []

    while pobli<=0.99:
        lis.append(process(pobli))
        pobli += pobli_step

    return lis

def avg(lis):
    a = []

    for i in lis:
        for ii in i:
            if ii:
                a.append(ii)
                break

    avglis = sum(a)/len(a)
    # print(a)
    print(min(a))
    print(avglis)

def main():
    global pobli

    avg(pobliplus(pobli))


if __name__ == '__main__':
    main()
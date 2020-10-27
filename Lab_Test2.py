import math
import sys
import random as r
import numpy as np
from numpy import random

def func1(x,y):
    if x == 1:
        if y == 1:
            return(1)
        else:
            return(0)    
    else:
        return(1)        

def func2(x,y):
    if x==1:
        return(1)
    else:
        if y==1:
            return(1)
        else:
            return(0)        

def func3(x,y):
    if x==1 & y==1:
        return(0)
    else:
        return(1)

def func(a,b,c,d):
    dz=0
    F1=func1(a,d)
    F2=func2(c,b)
    F3=func3(c,d)
    F4=func3(d,b)
    F5=func3(a,d)
    if F1==1:
        dz+=1
    if F2==1:
        dz+=1
    if F3==1:
        dz+=1  
    if F4==1:
        dz+=1
    if F5==1:
        dz+=1  
    return dz               


def simulated_annealing(a,b,c,d):
    E_curr=func(a,b,c,d)
    T=1000
    print("a\tb\tc\td\tT")
    print(f"{a}\t{b}\t{c}\t{d}\t{T}")
    n=np.random.uniform(0.0,1.0,100)
    for i in range(50):
        E_next=E_curr
        a1=a
        b1=b
        c1=c
        d1=d
        g=np.random.choice(n,1)
        l=r.randint(0,1)
        m=r.randint(2,3)
        if l==0:
            if a==1:
               a=0
            else:
                a=1  
        else:
            if b==1:
                b=0  
            else:
                b=1

        if m==1:
            if c==1:
                c=0
            else:
                c=1
        else:
            if d==1:
                d=0
            else:
                d=1  
        E_curr=func(a,b,c,d) 
        E_change=E_curr-E_next  
        if E_change > 0:
            T=T-10
            print(f"{a}\t{b}\t{c}\t{d}\t{T}")
        elif E_change == 0:
            w= (1/(1+math.exp(0)))  
            if w < g:
                a=a1
                b=b1
                c=c1
                d=d1
            elif w > g:
                T=T-10 
                print(f"{a}\t{b}\t{c}\t{d}\t{T}")   
        elif E_change < 0:
                a=a1
                b=b1
                c=c1
                d=d1

def main():
    simulated_annealing(1,1,1,1)     

if __name__ == "__main__": 
    main() 




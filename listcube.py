#!/usr/local/bin/python3

"""
 _ _     _             _                        
| (_)___| |_ ___ _   _| |__   ___   _ __  _   _ 
| | / __| __/ __| | | | '_ \ / _ \ | '_ \| | | |
| | \__ \ || (__| |_| | |_) |  __/_| |_) | |_| |
|_|_|___/\__\___|\__,_|_.__/ \___(_) .__/ \__, |
                                   |_|    |___/ 

this is listcube - an attempt to do the cubesum problem without
loops, using higher-order functions
"""

from functools import reduce

def cube(n):
  return(n*n*n)

def add(n, m):
  return(n + m)

def num2list(n):
  if(n == 0):
    return([])
  else:
    return(num2list(n // 10) + [n % 10])
  
def chknum(n):
  return(n == (reduce(add, map(cube, num2list(n)))))

def process():
  l1 = range(100,1000)
  l2 = filter(chknum, l1)
  print(list(l2))

if __name__ == '__main__':
  process()

#!/usr/local/bin/python3

"""
                 _ _   _            _                        
 _ __ ___  _   _| | |_(_) ___ _   _| |__   ___   _ __  _   _ 
| '_ ` _ \| | | | | __| |/ __| | | | '_ \ / _ \ | '_ \| | | |
| | | | | | |_| | | |_| | (__| |_| | |_) |  __/_| |_) | |_| |
|_| |_| |_|\__,_|_|\__|_|\___|\__,_|_.__/ \___(_) .__/ \__, |
                                                |_|    |___/ 

this is multicube - an attempt to do the cubesum problem in a 
multithreaded environment.
"""

from multiprocessing import Pool as ThreadPool
from multiprocessing import cpu_count

def cube(n):
  return(n*n*n)

def check(h,t,u):
  cusum = cube(h) + cube(t) + cube(u)
  num = (h*100) + (t*10)+u
  return(cusum == num, num)

def tucube(h):
  print(h)
  num = 0
  for t in range(10):
    for u in range(10):
      hit, num = check(h, t, u)
      if hit:
        print(num)

def process():
  print("Starting...")
  pool = ThreadPool(10)
  # rg = list(range(1,10))
  rg = list(range(9,0,-1))
  process = pool.map(tucube, rg)
  pool.close()
  pool.join()
  print("Complete.")

if __name__ == '__main__':
  process()


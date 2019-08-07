#!/usr/bin/python3

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

def cube(n):
  return(n*n*n)

def check(h,t,u):
  cusum = cube(h) + cube(t) + cube(u)
  num = (h*100) + (t*10)+u
  return(cusum == num, num)

def tucube(h):
  num = 0
  for t in range(10):
    for u in range(10):
      hit, num = check(h, t, u)
      if hit:
        print(num)

def process():
  for i in range(1,10):
    print(i)
    tucube(i)

if __name__ == '__main__':
  process()
      

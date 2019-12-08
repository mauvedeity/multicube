#!/usr/local/bin/python3

"""
 _ _     _                            
| (_)___| |_ ___ ___  _ __ ___  _ __  
| | / __| __/ __/ _ \| '_ ` _ \| '_ \ 
| | \__ \ || (_| (_) | | | | | | |_) |
|_|_|___/\__\___\___/|_| |_| |_| .__/ 
                               |_|    

this is listcomp - an attempt to do the cubesum problem using a list comprehension,
which is the most 'pythonic' way to do it. And it's (almost) a one-liner - who knew?
"""

def cube(n):
  return(n*n*n)

def mknum(x, y, z):
  return((x * 100) + (y * 10) + z)

def process():
  print([mknum(h,t,u) for h in range(1,10) for t in range(0,10) for u in range(0,10) if cube(h) + cube (t) + cube(u) == mknum(h,t,u)])

if __name__ == '__main__':
  process()

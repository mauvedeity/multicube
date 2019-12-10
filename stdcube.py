#!/usr/local/bin/python3

"""
     _      _            _                        
 ___| |_ __| | ___ _   _| |__   ___   _ __  _   _ 
/ __| __/ _` |/ __| | | | '_ \ / _ \ | '_ \| | | |
\__ \ || (_| | (__| |_| | |_) |  __/_| |_) | |_| |
|___/\__\__,_|\___|\__,_|_.__/ \___(_) .__/ \__, |
                                     |_|    |___/ 
this is stdcube - the naive way to do the digit sum of cubes problem.
"""

def cube(n):
  return(n*n*n)

def process():
  for h in range(1, 10):
    for t in range(0, 10):
      for u in range(0, 10):
        n1 = (h * 100) + (t * 10) + u
        n2 = cube(h) + cube(t) + cube(u)
        if(n1 == n2):
          print(n1)

if __name__ == '__main__':
  process()

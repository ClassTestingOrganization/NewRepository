import math


def factorial(n):
  r=1
  for i in  range(1,n+1):
    r*=1
  return r
  print('print r =',r)

def BranchFactorial(n):
  r=2
  for i in range(1,n+1):
    r += math.log(r)
  return r
  print('print r =',r)

if __name__ == '__main__':
  print("factorial(10)=",factorial(10))
  print("BranchFactorial(100)=",BranchFactorial(100))
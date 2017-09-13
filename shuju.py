# def score():
#     x = int(input("please input your score:"))
#     if 90<=x<=100:
#         print("score grade: A")
#     elif 70<=x<=89:
#         print("score grade: B")
#     elif 60<=x<=69:
#         print("score grade: C")
#     elif 0<=x<=59:
#         print("score grade: D")
#     else:
#         print("others Invalid score")
# score()
# import math
# def isPrime(n):
#   if n <= 1:
#     return False
#   i = 2
#   while i*i <= n:
#     if n % i == 0:
#       return False
#     i += 1
#   return True
# def primelist(x):
#     n1 = [i for i in range(2, x) if isPrime(i)]
#     return n1
# n2 = list(range(4,2000,2))
# sum = 0
# for n in n2:
#     for i in primelist(n):
#         for y in primelist(n):
#             if n == y + i:
#                 sum += 1
#                 if sum % 6 ==0:print("\n")
#                 print(str(n)+"="+str(y)+"+"+str(i)+"  ",end="")

def isPrime(n):
  if n <= 1:
    return False
  i = 2
  while i*i <= n:
    if n % i == 0:
      return False
    i += 1
  return True
def primelist(x):
    n1 = [i for i in range(2, x) if isPrime(i)]
    return n1
def numprime(n,y):
    sum = 0
    for x in primelist(y):
        M = 2 ** x - 1
        if isPrime(M):
            sum += 1
            print(M,x)
        if sum % n ==0:
            break
numprime(6,100)
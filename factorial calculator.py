n = int(input())
def factorial(n):
    if n == 1:
        f =1
        print(f)
    else :
        ft = 1
        for i in range(1,n+1):
            ft = ft*i
        print(ft)
factorial(n)

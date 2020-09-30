
a=int(input())
for _ in range(int(input())):
    n,r = map(int,input().split())
    r=r%n
    b = list(map(int, input().split()))
    b =(b[(n-r):n]+b[:(n-r)])
    s=""
    for i in b:
        if i != ",":
            s += str(i) + " "
    print(s)


N = int(input())
i = 1
start = 1
mid = -1
if N%2==0:
    mid = N//2+1
else:
    mid = (N+1)//2
while i<=N:
    compl = N-i
    if i <= compl:
        k = start
        for j in range(1,N+1):
            print(k,end=" ")
            k+=1
        start = k+N
    elif i==mid:
        for j in range(N*N-(N-1),N*N+1):
            print(j,end=" ")
    elif(i>compl and compl !=0):
        k = 2*N + (compl)*(N+1) + (N-1) * (compl-1)
        for j in range(1,N+1):
            print(k,end=" ")
            k+=1
    else:
        for k in range(N+1,2*N+1):
            print(k,end=" ")
    i+=1
    print()
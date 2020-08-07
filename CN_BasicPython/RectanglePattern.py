N = int(input())

for i in range(1,2*N):
    k=N
    for j in range(1,2*N):
        print(k,end=" ")
        if i>j:
            k-=1
        if i+j>=2*N:
            k+=1
    print()
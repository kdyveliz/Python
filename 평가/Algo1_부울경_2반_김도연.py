T = int(input())
for tc in range(1,T+1):
    N = int(input())
    decal = list(input())
    length = 0
    ans = 1
    for i in range(N):
        for j in range(1,N):
            if i+j < N and 0 <= i-j:
                if decal[i+j] == decal[i-j]:
                    length = (j*2)+1
                    ans = max(ans,length)
                else:
                    ans = max(ans,length)
                    break
    print(f'#{tc} {ans}')
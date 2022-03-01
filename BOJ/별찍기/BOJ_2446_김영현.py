n = int(input())

# for 문 안에 if 문
for i in range(2*n-1):
    if i < n :
        print(' ' * i + '*' * ((2*n) - ((2*i)+1)))
    else:
        print(' ' * (n - (i-n+2)) + '*' * (2*(i-n) + 3))

# for 문 2번
# for i in range(n):
#     print(' ' * i + '*' * ((2*n) - ((2*i)+1)))

# for i in range(n-1):
#     print(' ' * (n-i-2) + '*' * ((2*i)+3))
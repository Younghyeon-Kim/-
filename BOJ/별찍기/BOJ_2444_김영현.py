n = int(input())

# for 문 안에 if 문
# for i in range(2*n-1):
#     if i < n:
#         print((' ' * (n-(i+1))) + ('*' * ((2*i)+1)))
#     else:
#         print((' ' * (i-(n-1))) + ('*' * ((2*n)-((2*(i-(n-1)))+1))))


# for 문 2번
for i in range(n):
    print((' ' * (n-(i+1))) + ('*' * ((2*i)+1)))

for i in range(n-1):
    print((' ' * (i+1)) + ('*' * ((2*(n-1)) - ((2*i)+1))))
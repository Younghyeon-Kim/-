n = int(input())
j = 0

for i in range(1, n+1):
    print((' ' * (n-i)) + ('*' * (i+j)))
    j += 1
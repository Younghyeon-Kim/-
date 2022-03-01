# 별을 찍어줄 함수를 만든다
def drawing_stars(n):
    # 별을 찍을 리스트를 할당
    paper = []
    for i in range(3 * len(n)):
        # n이 3으로 나누어 떨어지지 않으면 n의 길이 만큼 공백
        if i // len(n) == 1:
            paper.append(n[i % len(n)] + ' ' * len(n) +n[i % len(n)])
        
        else:
            paper.append(n[i % len(n)] * 3)
    
    return paper

stars = ['***', '* *', '***']
n = int(input())
k = 0

# n이 3이 될 때까지 n을 3으로 나눈 값을 다시 n값으로 할당
while n != 3:
    n = int(n / 3)
    # 함수를 몇번 실행할지 정하는 변수
    k += 1

for i in range(k):
    stars = drawing_stars(stars)
for i in stars:
    print(i)
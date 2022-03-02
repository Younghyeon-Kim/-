# 별을 찍어줄 함수를 만든다
def drawing_stars(stars):
    # 별을 찍을 리스트를 할당
    paper = []
    for i in range(3 * len(stars)):
        # n이 3으로 나누어 떨어지지 않으면 n의 길이 만큼 공백
        if i // len(stars) == 1:
            paper.append(stars[i % len(stars)] + ' ' * len(stars) +stars[i % len(stars)])
        
        else:
            paper.append(stars[i % len(stars)] * 3)
    
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
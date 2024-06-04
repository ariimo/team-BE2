import random
user_input = int(input("몇 번 실행할 건지 입력하세요 : "))

win = 0
for i in range(user_input):
    prize = random.randint(1, 3)
    choice = 1
    # 홍식
    if prize == choice:
        open = 2
        choice = 3
    if prize == choice:
    # 아림
    elif prize == 2:
    # 인제
    else:
        open = 2
        choice = 3
        win += 1
# 민규
print('몬티홀 실험, {}번 시도, 만약 문을 바꾼다면, {}번 이긴다, {}% 확률 {} 시도'.format(user_input, win, 100 * win / user_input, user_input))
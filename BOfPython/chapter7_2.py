숫자 = 23
작동 = True

while 작동:
    답변 = int(input("숫자를 입력하세요 : "))

    if  답변 == 숫자:
        print("축하합니다 숫자르 맞췄습니다")
        작동 = False
    elif 답변 < 숫자:
        print("틀렸어요 숫자가 좀더 커야합니다")
    else:
        print("틀렸어요 숫자가 좀더 작아야 합니다")
else:
    print("whil 루프가 끝났습니다")

print("끝")
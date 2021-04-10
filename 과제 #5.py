from random import *
cus = 0
for i in range(1,51) :
    time = randrange(5,51)
    if 5 <= time <= 15 :
        cus +=1
    print(str(i) + "번째 손님 (소요시간 : " + str(time) + "분)")

print("총 탑승 승객 :", str(cus)+"분")
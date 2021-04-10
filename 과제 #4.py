from random import *
#1부터 20까지 리스트 생성
nums = range(1,21)
nums = list(nums)
shuffle(nums)

#당첨자 4명 선발
jackpot = sample(nums, 4)

#4명 중 치킨 당첨자 1명 선발
shuffle(jackpot)
lotto = randint(0,3)
chicken = jackpot[lotto]

#4명 리스트에서 치킨 당첨자 제거
jackpot.remove(jackpot[lotto])
jackpot.sort()

#당첨자 발표
print("-- 당첨자 발표 --")
print("치킨 당첨자: " + str(chicken))
print("커피 당첨자: " + str(jackpot))
print("-- 축하합니다 --")

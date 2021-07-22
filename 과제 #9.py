'''
조건1: 1보다 작거나 숫자가 아닌 입력밧이 들어올 때는 ValueError로 처리
        출력 메시지: "잘못된 값을 입력하였습니다."
조건2: 대기 손님이 주문할수 있는 총 치킨량을 10마리로 한정
        치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
        출력 메시지: "재고가 소진되어 더 이상 주문을 받지 않습니다."
'''

class SoldOutError(Exception) :
    pass

chicken = 10
waiting = 1

while True :
    try :
        print("[남은 치킨] : {0}".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order < 1 or type(order) != int :
            raise ValueError
        elif order > chicken :
            print("재료가 부족합니다.")
        else :
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0 :
            raise SoldOutError
    except ValueError :
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError :
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break